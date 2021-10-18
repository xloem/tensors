def common_members(TENSOR_CLASSES = [], **kw):
    '''
    Define and return common members for backend modules.

    :param kw: **locals() from the backend
    :returns: A dict of common members to add
    '''
    del kw

    def is_backend(tensor):
        '''
        Identify whether a tensor belongs to this backend.
    
        :param tensor: tensor to check
        :returns: True if the tensor belongs to this backend
        '''
        for cls in TENSOR_CLASSES:
            if isinstance(tensor, cls):
                return True
        return False

    def to_backend(tensor):
        '''
        Convert a tensor to this backend

        :param tensor: tensor to convert
        :returns: tensor in backend-specific format
        '''
        from . import get_backend
        # dlpack is a universal tensor interchangen standard
        dlpack = get_backend(tensor).dlpack.to_dlpack(tensor)
        return backend.dlpack.from_dlpack(dlpack)
    return locals()

def add_common_members(locals):
    '''
    Add common members to a backend.
    
    :param locals: locals() from within the backend
    '''
    __all__ = locals.setdefault('__all__', list(locals.keys()))
    members = common_members(**locals)
    __all__.extend(members.keys())
    locals.update(members)
