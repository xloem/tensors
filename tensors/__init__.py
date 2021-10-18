import tensors.jax, tensors.torch

TENSOR_CLASS_BACKENDS = {}

def get_backend(tensor):
    '''
    Get the backend module for a tensor.

    :param tensor: tensor to find backend for
    :returns: backend module
    '''
    return TENSOR_CLASS_BACKENDS[type(tensor)]

for backend in tensors.jax, tensors.torch:
    TENSOR_CLASS_BACKENDS[backend.Tensor] = backend
    for member in dir(backend):
        if backend.name in member and backend.name != member:
            locals()[member] = getattr(backend, member)

# ensures manually added functions are listed in documentation
__all__ = list(locals().keys())
