
import tensors.jax, tensors.torch
backends = [tensors.jax, tensors.torch]


backends_by_tensor_class = {}

def get_backend(tensor):
    '''
    Get the backend module for a tensor.

    :param tensor: tensor to find backend for
    :returns: backend module
    '''
    return backends_by_tensor_class[type(tensor)]

for backend in backends:
    backends_by_tensor_class[backend.Tensor] = backend
    for member in dir(backend):
        if backend.name in member and backend.name != member:
            locals()[member] = getattr(backend, member)

from . import tensor

# ensures manually added functions are listed in documentation
__all__ = list(locals().keys())
