def common_members(
        Tensor : type,
        dlpack,
        __name__ : str = '',
         **kw
    ) -> dict:
    '''
    Define and return common members for backend modules.

    :param kw: **locals() from the backend
    :returns: A dict of common members to add
    '''
    del kw
    print(__name__)
    name = __name__.split('.')[-1]

    def is_backend(tensor) -> bool:
        '''
        Identify whether a tensor is from this backend
        '''
        return isinstance(tensor, Tensor)

    def to_backend(tensor) -> Tensor:
        '''
        Convert a tensor to this backend
        '''
        from . import get_backend
        # dlpack is a universal tensor interchangen standard
        dlpack = get_backend(tensor).dlpack.to_dlpack(tensor)
        return dlpack.from_dlpack(dlpack)

    return locals()

def add_common_members(locals : dict):
    '''
    Add common members to a backend.
    
    :param locals: locals() from within the backend
    '''
    __all__ = locals.setdefault('__all__', list(locals.keys()))
    members = common_members(**locals)
    for name, member in [*members.items()]:
        if hasattr(member, '__doc__') and member.__doc__ is not None:
            if 'this backend' in member.__doc__:
                member.__doc__ = member.__doc__.replace('this backend', members['name'])
        if '_backend' in name:
            name2 = name.replace('_backend', '_' + members['name'])
            members[name2] = member
    locals.update(members)
    __all__.extend(members.keys())
