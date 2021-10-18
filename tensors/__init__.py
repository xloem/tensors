
from . import _backend

def get_backend(tensor):
    '''
    Get the backend module for a tensor.

    :param tensor: tensor to find backend for
    :returns: backend module
    '''
    Tensor = type(tensor)
    # first see if it's quickly available
    try:
        return _backend.backends_by_tensor_class[Tensor]
    except:
        pass

    # now load new things, try more
    _backend.load_new_backends()
    try:
        return _backend.backends_by_tensor_class[Tensor]
    except:
        pass
    for cls, backend in _backend.backends_by_tensor_class.items():
        if issubclass(Tensor, cls):
            _backend.backends_by_tensor_class[Tensor] = backend
            return backend
    raise

locals().update(_backend.get_global_stubs())

_backend.load_new_backends()

if len(_backend.backends_by_name) == 0:
    # ensure at least one backend is loaded
    for backend_name in _backend.backend_names:
        try:
            _backend.load_backend_by_name(backend_name)
            _last_loading_exception = None
            break
        except Exception as e:
            _last_loading_exception = e
            pass
    if _last_loading_exception is not None:
        _last_loading_exception.args = ("Failed to load any backend among " + ", ".join(_backend.backend_names), *_last_loading_exception.args)
        raise _last_loading_exception

for _backend_name, default in _backend.backends_by_name.items():
    locals()[_backend_name] = default
_backend.set_default(default)

# using __all__ ensures procedurally added functions are listed in documentation
__all__ = [name for name in locals().keys() if name[0] != '_']
