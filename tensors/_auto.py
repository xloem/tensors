import inspect

def member_map_of(obj, public_only=True, **maps):
    for member_name in dir(obj):
        if public_only and member_name[0] == '_':
            continue
        impl_member_name = maps.get(member_name, member_name)
        member = getattr(obj, member_name)
        yield member_name, impl_member_name, member

def wrap_func(func, impl_str, filename, locals={}, globals={}, return_wrap_str=None, **maps):
    sig = inspect.signature(func)
    strsig = str(sig)
    impl_params = []
    kw_params = []
    for paramname in sig.parameters:
        if paramname in maps:
            kwparams.append(f'{maps[paramname]} = {paramname}')
        else:
            impl_params.append(paramname)
    impl_params.extend(kw_params)
    impl_params = ', '.join(impl_params)

    if return_wrap_str is not None and "Returns" in member.__doc__:
        return_wrap_prefix = return_wrap_str + '('
        return_wrap_postfix = ')'
    else:
        return_wrap_prefix = ''
        return_wrap_postfix = ''

    exec(compile(f"""
        def {member_name}{strsig}:
            \"\"\"{member.__doc__}\"\"\"
            return {return_wrap_prefix}{impl_str}({impl_params}){return_wrap_postfix}
    """, filename, "exec"), globals, locals)
    return locals[member_name]

def guesswrap(filename, mod, cls, **maps):
    import arrays_api

    Array_name = cls.__name__

    result = {}

    for member_name, impl_member_name, member in member_map_of(arrays_api, **maps):
        if member is arrays_api.Array:
            continue
        if type(member) is float:
            result[member_name] = member
            continue

        submod = mod
        while '.' in impl_member_name:
            modname, impl_member_name = impl_member_name.split('.', 1)
            submod = getattr(submod, modname)
        if not hasattr(submod, impl_member_name):
            raise NotImplementedError(f"{mod} map not specified properly for member {member_name}.  Other members may work if this check is removed.")

        # functions that return something can be wrapped in Array

        wrap_func(member, 'mod.' + impl_member_name, filename, result, globals=dict(impl=mod), return_wrap_str=Array_name, **maps)

    class Array:
        def __init__(self, src):
            if isinstance(src, cls):
                self._data = src
            else:
                raise NotImplementedError

        for member_name, member in result.items():
            if member is getattr(arrays_api.creation_functions, member_name):
                member = staticmethod(member)
            locals()[member_name] = member

        for member_name, impl_member_nam, member in member_map_of(arrays_api.Array, public_only = False, **maps):
            if not hasattr(cls, impl_member_name):
                raise NotImplementedError(f"{cls} map not specified for array member {member_name}.  Other members may work if this check is removed.")
            if type(member) is property:
                exec(compile(f"""
                    @property
                    def {member_name}(self):
                       return self._data.{impl_member_name}
                """, filename, "exec"), locals())
            else:
                wrap_func(member, 'self._data.' + impl_member_name, filename, locals(), return_wrap_str=Array_name, **maps)
        del member_name
        del impl_member_name
        del member

    result[Array_name] = Array
    return result
