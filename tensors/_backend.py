backend_names = set(('jax', 'torch'))

def load_backend_by_name(name : str):
    if name == 'jax':
        import tensors.jax as backend
    elif name == 'torch':
        import tensors.torch as backend
    else:
        raise Exception('Unknown backend: ' + name)
    if name not in backends_by_name:
        register(backend)
    return backend

backends_by_name = {}
backends_by_tensor_class = {}

def register(backend):
    '''
    Registers a backend after it is loaded.
    '''
    backends_by_tensor_class[backend.Tensor] = backend
    backends_by_name[backend.name] = backend

    import tensors

    #setattr(tensors.tensor, backend.name, backend.tensor)
    try:
        tensors.__all__.extend(backend.name)
    except Exception:
        # still importing
        pass

    for member in dir(backend):
        if backend.name in member and backend.name != member:
            setattr(tensors, member, getattr(backend, member))

def set_default(backend):
    import tensors
    tensors.default = backend
    #for name, member in backend.__dict__.items():
    #    if name[0] != '_' and callable(member):
    #        setattr(tensors, name, member)

def load_new_backends():
    '''
    Enumerates loaded tensor packages and imports a tensors backend for any new ones found.

    :returns: list of new tensors backend modules
    '''
    import sys

    new_backends = backend_names.difference(backends_by_name.keys())
    new_backends.intersection_update(sys.modules.keys())

    new_backends = [load_backend_by_name(name) for name in new_backends]
    return new_backends

def common_members(
        Tensor : type,
        tensor : callable,
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
    name = __name__.split('.')[-1]

    @backend_doc(name)
    def is_backend(tensor) -> bool:
        '''
        Identify whether a tensor is from this backend
        '''
        return isinstance(tensor, Tensor)

    @backend_doc(name)
    def to_backend(foreign_tensor) -> Tensor:
        '''
        Convert a tensor to this backend
        '''
        from . import get_backend
        # dlpack is a universal tensor interchangen standard
        dlpack_tensor = get_backend(foreign_tensor).dlpack.to_dlpack(foreign_tensor)
        return dlpack.from_dlpack(dlpack_tensor)

    tensor_backend = tensor

    return locals()

def backend_doc(name):
    def mutate_doc(func):
        if func.__doc__ is not None and 'this backend' in func.__doc__:
            func.__doc__ = func.__doc__.replace('this backend', name)
        return func
    return mutate_doc

def add_common_members(locals : dict):
    '''
    Add common members to a backend.
    
    :param locals: locals() from within the backend
    '''
    __all__ = locals.setdefault('__all__', list(locals.keys()))
    members = common_members(**locals)
    for name, member in [*members.items()]:
        if 'backend' in name:
            name2 = name.replace('backend', members['name'])
            members[name2] = member
    locals.update(members)
    __all__.extend(members.keys())

def get_global_stubs():
    '''
    Create and return wrapper functions for backend-named functions.

    Each one, when called, imports the backend and hands its parameters off.

    :returns: dict of functions
    '''
    results = {}
    def stub(backend_name, function_name):
        def wrapper(*params, **kwparams):
            '''
            Backend will be loaded when called.  No documentation yet.
            '''
            backend = load_backend_by_name(backend_name)
            func = getattr(backend, function_name)
            return func(*params, **kwparams)
        return wrapper
    for name in common_members(None, None, None):
        if 'backend' in name:
            for backend_name in backend_names:
                backend_func_name = name.replace('backend', backend_name)
                results[backend_func_name] = stub(backend_name, name)
    return results
