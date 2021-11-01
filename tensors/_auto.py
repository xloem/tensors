import inspect, types

def member_map_of(obj, public_only=True, **maps):
    for member_name in dir(obj):
        if public_only and member_name[0] == '_':
            continue
        impl_member_name = maps.get(member_name, member_name)
        member = getattr(obj, member_name)
        yield member_name, impl_member_name, member

def wrap_func(func, impl_str, filename, locals={}, globals={}, return_wrap_str=None, **maps):
    func_name = func.__name__
    sig = inspect.signature(func)
    strsig = str(sig)
    impl_params = []
    kw_params = []
    for paramname in sig.parameters:
        if paramname in maps:
            kw_params.append(f'{maps[paramname]} = {paramname}')
        else:
            impl_params.append(paramname)
    impl_params.extend(kw_params)
    impl_params = ', '.join(impl_params)

    if return_wrap_str is not None and "Returns" in func.__doc__:
        return_wrap_prefix = return_wrap_str + '('
        return_wrap_postfix = ')'
    else:
        return_wrap_prefix = ''
        return_wrap_postfix = ''

    exec(compile(inspect.cleandoc(f"""
        def {func_name}{strsig}:
            \"\"\"{func.__doc__.replace(chr(10),'''
            ''')}\"\"\"
            return {return_wrap_prefix}{impl_str}({impl_params}){return_wrap_postfix}
    """), filename, "exec"), globals, locals)
    return locals[func_name]

def guesswrap(filename, mod, cls, **maps):
    import arrays_api

    Array_name = cls.__name__

    result = {}

    for member_name, impl_member_name, member in member_map_of(arrays_api, **maps):
        if member is arrays_api.Array:
            continue
        if type(member) in (float, types.ModuleType):
            result[member_name] = member
            continue

        submod = mod
        sub_impl_member_name = impl_member_name
        while '.' in sub_impl_member_name:
            modname, sub_impl_member_name = sub_impl_member_name.split('.', 1)
            submod = getattr(submod, modname)
        if not hasattr(submod, impl_member_name):
            found = False
            for obj_member_name, obj_impl_member_name, obj_member in member_map_of(arrays_api.Array, public_only = False, **maps):
                if obj_member.__doc__ is not None and member_name in obj_member.__doc__:
                    found = True
                    break
            if found:
                wrap_func(member, Array_name + '.' + obj_member_name, filename, result)
            else:
                if callable(member):
                    print('MISSING:', member_name + str(inspect.signature(member)) + ':')
                    print(member.__doc__)
                else:
                    print('MISSING:', member_name)
                locals()[member_name] = member
                #raise NotImplementedError(f"{mod.__name__} map not specified properly for member {member_name}.  Other members may work if this check is removed.")
        elif member is NotImplemented:
            exec(compile(f'{member_name} = impl.' + impl_member_name, filename, 'exec'), dict(impl=mod), result)
        else:
            wrap_func(member, 'impl.' + impl_member_name, filename, result, globals=dict(impl=mod), return_wrap_str=Array_name, **maps)
            

    outer_scope = locals()
    class _Empty:
        pass
    class Array:
        def __init__(self, src):
            if isinstance(src, cls):
                self._data = src
            else:
                raise NotImplementedError

        wrap_func(arrays_api.Array.__array_namespace__, 'self #', filename, locals())

        for member_name, member in result.items():
            if member is getattr(arrays_api.creation_functions, member_name, None):
                member = staticmethod(member)
            locals()[member_name] = member

        for member_name, impl_member_name, member in member_map_of(arrays_api.Array, public_only = False, **maps):
            if hasattr(_Empty, member_name):
                continue
            for test, prefix in (('cls.','self._data.'), ('mod.','impl.'), (None,None)):
                try:
                    if eval(compile(test + impl_member_name, filename, 'eval'), outer_scope) is not None:
                        break
                except:
                    pass
            if prefix is None:
                if member_name in locals():
                    continue
                else:
                    if callable(member):
                        print('MISSING:', member_name + str(inspect.signature(member)) + ':')
                    else:
                        print('MISSING:', member_name)
                    print(member.__doc__)
                    #raise NotImplementedError(f"{cls} map not specified for array member {member_name}.  Other members may work if this check is removed.")
            elif type(member) is property:
                exec(compile(inspect.cleandoc(f"""
                    @property
                    def {member_name}(self):
                       return self._data.{impl_member_name}
                """), filename, "exec"), locals())
            else:
                wrap_func(member, prefix + impl_member_name, filename, locals(), globals=dict(impl=mod), return_wrap_str=Array_name, **maps)
        del member_name
        del impl_member_name
        del member

    result[Array_name] = Array
    return result
