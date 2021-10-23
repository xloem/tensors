def broadcast_arrays(*arrays):
    """Broadcasts one or more arrays against one another.
    Parameters
    **********
    
    *   **arrays**: *<array>*
    
        *   an arbitrary number of to-be broadcasted arrays.
    Returns
    *******
    
    *   **out**: *List[ <array> ]*
    
        *   a list of broadcasted arrays. Each array must have the same
            shape. Each array must have the same dtype as its
            corresponding input array."""
    raise NotImplemented

def broadcast_to(x, /, shape):
    """Broadcasts an array to a specified shape.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   array to broadcast.
    
    *   **shape**: *Tuple[int, …]*
    
        *   array shape. Must be compatible with ``x`` (see `Broadcasting
            <#broadcasting>`_).
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array having a specified shape. Must have the same data
            type as ``x``.
    Raises
    ******
    
    *   if the array is incompatible with the specified shape (see
        `Broadcasting <#broadcasting>`_)."""
    raise NotImplemented

def can_cast(from_, to, /):
    """Determines if one data type can be cast to another data type according
    `Type Promotion Rules <#type-promotion>`_ rules.
    Parameters
    **********
    
    *   **from_**: *Union[ <dtype>, <array>]*
    
        *   input data type or array from which to cast.
    
    *   **to**: *<dtype>*
    
        *   desired data type.
    Returns
    *******
    
    *   **out**: *bool*
    
        *   ``True`` if the cast can occur according to `Type Promotion
            Rules <#type-promotion>`_ rules; otherwise, ``False``."""
    raise NotImplemented

def finfo(type, /):
    """Machine limits for floating-point data types.
    Parameters
    **********
    
    *   **type**: *Union[ <dtype>, <array> ]*
    
        *   the kind of floating-point data-type about which to get
            information.
    Returns
    *******
    
    *   **out**: *<finfo object>*
    
        *   an object having the following attributes:
    
            *   **bits**: *int*
    
                *   number of bits occupied by the floating-point data
                    type.
    
            *   **eps**: *float*
    
                *   difference between 1.0 and the next smallest
                    representable floating-point number larger than 1.0
                    according to the IEEE-754 standard.
    
            *   **max**: *float*
    
                *   largest representable number.
    
            *   **min**: *float*
    
                *   smallest representable number.
    
            *   **smallest_normal**: *float*
    
                *   smallest positive floating-point number with full
                    precision."""
    raise NotImplemented

def iinfo(type, /):
    """Machine limits for integer data types.
    Parameters
    **********
    
    *   **type**: *Union[ <dtype>, <array> ]*
    
        *   the kind of integer data-type about which to get information.
    Returns
    *******
    
    *   **out**: *<iinfo object>*
    
        *   a class with that encapsules the following attributes:
    
            *   **bits**: *int*
    
                *   number of bits occupied by the type
    
            *   **max**: *int*
    
                *   largest representable number.
    
            *   **min**: *int*
    
                *   smallest representable number."""
    raise NotImplemented

def result_type(*arrays_and_dtypes):
    """Returns the dtype that results from applying the type promotion rules
    (see `Type Promotion Rules <#type-promotion>`_) to the arguments.
    Note: If provided mixed dtypes (e.g., integer and floating-point), the
        returned dtype will be implementation-specific.
    Parameters
    **********
    
    *   **arrays_and_dtypes**: *Union[ <array>, <dtype> ]*
    
        *   an arbitrary number of input arrays and/or dtypes.
    Returns
    *******
    
    *   **out**: *<dtype>*
    
        *   the dtype resulting from an operation involving the input
            arrays and dtypes."""
    raise NotImplemented

