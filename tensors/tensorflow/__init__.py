from tensors.device import Device

import tensorflow as framework

from tensorflow import (
    constant as tensor,
    Tensor,

    range as arange,

    concat,
    stack,

    argmax,
    einsum,
)
from tensorflow.nn import (
    softmax,
)
from tensorflow.experimental import (
    dlpack
)

def hwaccel_present() -> bool:
    '''Returns a bool indicating whether GPU use is available.'''
    return bool([
        True
        for device in framework.config.list_physical_devices()
        if device.device_type != 'CPU'
    ])

def dev_of(tensor : Tensor) -> Device:
    host_task, type, index = tensor.device.rsplit(':', 3)
    return Device(
        host_task.rsplit('/', 1)[0],
        type.lower(),
        int(index)
    )

from .. import _backend
_backend.add_common_members(locals())
