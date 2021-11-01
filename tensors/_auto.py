import inspect, os, types

def member_map_of(obj, public_only=True, **maps):
    for member_name in dir(obj):
        if public_only and member_name[0] == '_':
            continue
        impl_member_name = maps.get(member_name, member_name)
        member = getattr(obj, member_name)
        yield member_name, impl_member_name, member

# uses in-memory generated source
# having source to debug would be helpful
# better:
#   - generate a file, or
#   - use static wrapper functions; can still be made per-function

def wrap_func(func, impl_str, filename, locals={}, globals={}, return_wrap_str=None, **maps):
    func_name = func.__name__
    sig = inspect.signature(func)
    strsig = str(sig)
    impl_params = []
    kw_params = []
    for paramname, paramval in sig.parameters.items():
        if paramname in maps:
            parammap = maps[paramname]
            if parammap is None:
                continue
            elif parammap.isidentifier():
                kw_params.append(f'{parammap} = {paramname}')
            else:
                impl_params.append(parammap)
        elif paramname != 'self':
            impl_params.append(paramname)
        if paramname in ('other','x','y'):
            impl_params[-1] += '._data'
    impl_params.extend(kw_params)
    impl_params = ', '.join(impl_params)

    if return_wrap_str is not None and "Returns" in func.__doc__:
        return_wrap_prefix = return_wrap_str + '('
        return_wrap_postfix = ')'
    else:
        return_wrap_prefix = ''
        return_wrap_postfix = ''

    #if func_name == 'asarray':
    #    import pdb; pdb.set_trace()
    exec(compile(inspect.cleandoc(f"""
        def {func_name}{strsig}:
            \"\"\"{func.__doc__.replace(chr(10),'''
            ''')}\"\"\"
            return {return_wrap_prefix}{impl_str}({impl_params}){return_wrap_postfix}
    """), filename, "exec"), globals, locals)
    return locals[func_name]

def guesswrap(filename, mod, Array_name, **maps):
    import arrays_api

    mod_name = mod.__name__
    result = {mod_name: mod}

    filemod_guess = os.path.splitext(os.path.basename(filename))[0]

    qualified_Array_name = mod_name + '.' + Array_name
    cls = eval(compile(qualified_Array_name, filename, 'eval'), result)


    for member_name, impl_member_name, member in member_map_of(arrays_api, **maps):
        if member is arrays_api.Array:
            continue
        if type(member) in (float, types.ModuleType):
            result[member_name] = member
            continue

        submod = mod
        if impl_member_name.isidentifier():
            sub_impl_member_name = impl_member_name
            impl_member_name = mod_name + '.' + impl_member_name
        else:
            sub_impl_member_name = member_name
        while '.' in sub_impl_member_name:
            modname, sub_impl_member_name = sub_impl_member_name.split('.', 1)
            submod = getattr(submod, modname)
        if not hasattr(submod, sub_impl_member_name):
            found = False
            for obj_member_name, obj_impl_member_name, obj_member in member_map_of(arrays_api.Array, public_only = False, **maps):
                if obj_member.__doc__ is not None and member_name in obj_member.__doc__:
                    found = True
                    break
            if found:
                wrap_func(member, qualified_Array_name + '.' + obj_member_name, filename, globals=result, locals=result)
            else:
                if callable(member):
                    print('MISSING:', member_name + str(inspect.signature(member)) + ':')
                    print(member.__doc__)
                else:
                    print('MISSING:', member_name)
                locals()[member_name] = member
                #raise NotImplementedError(f"{mod.__name__} map not specified properly for member {member_name}.  Other members may work if this check is removed.")
        elif member is NotImplemented:
            exec(compile(f'{member_name} = ' + impl_member_name, filename, 'exec'), result)
        else:
            funcmaps = {**maps}
            for key, val in maps.items():
                if key.startswith(member_name + '_'):
                    funcmaps[key[len(member_name)+1:]] = val
            return_wrap_str = '' if member_name in (
                'can_cast',
                'result_type'
            ) else Array_name
            wrap_func(member, impl_member_name, filename, globals=result, locals=result, return_wrap_str=return_wrap_str, **funcmaps)
            

    outer_scope = locals()
    class Array:
        def __init__(self, src):
            if isinstance(src, cls):
                self._data = src
            else:
                raise NotImplementedError(type(src))
        def __str__(self):
            return str(self._data)
        def __repr__(self):
            return filemod_guess.split('/')[-1].split('.',1)[0] + '.' + Array_name + '(' + repr(self._data) + ')'

        wrap_func(arrays_api.Array.__array_namespace__, 'self #', filename, locals=locals(), globals=result)

        for member_name, member in [*result.items()]:
            if member_name[0] == '_':
                del result[member_name]
                continue
            if member is getattr(arrays_api.creation_functions, member_name, None):
                member = staticmethod(member)
            locals()[member_name] = member

        for member_name, impl_member_name, member in member_map_of(arrays_api.Array, public_only = False, **maps):
            if member is None or member_name in (
                    '__dict__', '__class__', '__doc__', '__getattr__', '__getattribute__',
                    '__init__', '__init_subclass__', '__module__', '__new__', '__setattr__',
                    '__subclasshook__', '__weakref__',
            ):
                continue
            print(member_name)
            for test, prefix in (('cls.','self._data.'), ('mod.',mod_name + '.'), (None,None)):
                try:
                    if eval(compile(test + impl_member_name, filename, 'eval'), outer_scope) is not None:
                        break
                except:
                    pass

            return_wrap_str = '' if member_name in (
                '__bool__', '__dlpack__', '__dlpack_device__', '__float__', '__index__', '__int__',
                'device', 'dtype', 'ndim', 'shape', 'size'
            ) else Array_name

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
                       return {prefix}{impl_member_name}
                """), filename, "exec"), locals())
            else:
                wrap_func(member, prefix + impl_member_name, filename, locals=locals(), globals=result, return_wrap_str=return_wrap_str, **maps)
        del member_name
        del impl_member_name
        del member

    Array.__name__ = Array_name
    result[Array_name] = Array
    return result
