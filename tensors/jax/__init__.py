import jax as framework
import jaxlib

from jax.numpy import (
    array as tensor,

    arange,

    concatenate as concat,
    stack,

    argmax,
    einsum,
)
from jax.nn import (
    softmax
)
from jax import (
    dlpack
)

def hwaccel_present() -> bool:
    '''Returns a bool indicating whether GPU/TPU use is available.'''
    # jax always prefers to connect to an accelerator if there is one
    return framework.default_backend() != 'cpu'

Tensor = jaxlib.xla_extension.DeviceArray

from .. import _backend
_backend.add_common_members(locals())
