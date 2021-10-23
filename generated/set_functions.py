def unique_all(x, /):
    """Data-dependent output shape: The shapes of two of the output arrays
    for this function depend on the data values in the input array; hence,
    array libraries which build computation graphs (e.g., JAX, Dask, etc.)
    may find this function difficult to implement without knowing array
    values. Accordingly, such libraries may choose to omit this function.
    See data-dependent-output-shapes section for more details.
    Returns the unique elements of an input array ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. If ``x`` has more than one dimension, the
            function must flatten ``x`` and return the unique elements of
            the flattened array.
    Returns
    *******
    
    *   **out**: *Tuple[ <array>, <array>, <array>, <array> ]*
    
        *   a namedtuple ``(values, indices, inverse_indices, counts)``
            whose
    
            *   first element must have the field name ``values`` and must
                be an array containing the unique elements of ``x``. The
                array must have the same data type as ``x``.
    
            *   second element must have the field name ``indices`` and
                must be an array containing the indices (first
                occurrences) of ``x`` that result in ``values``. The array
                must have the same shape as ``values`` and must have the
                default integer data type.
    
            *   third element must have the field name ``inverse_indices``
                and must be an array containing the indices of ``values``
                that reconstruct ``x``. The array must have the same shape
                as ``x`` and must have the default integer data type.
    
            *   fourth element must have the field name ``counts`` and
                must be an array containing the number of times each
                unique element occurs in ``x``. The returned array must
                have same shape as ``values`` and must have the default
                integer data type.
    
            Note: The order of unique elements is not specified and may vary
                between implementations."""
    raise NotImplemented

def unique_inverse(x, /):
    """Returns the unique elements of an input array ``x`` and the indices
    from the set of unique elements that reconstruct ``x``.
    Data-dependent output shape: The shape of one of the output arrays for
    this function depends on the data values in the input array; hence,
    array libraries which build computation graphs (e.g., JAX, Dask, etc.)
    may find this function difficult to implement without knowing array
    values. Accordingly, such libraries may choose to omit this function.
    See data-dependent-output-shapes section for more details.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. If ``x`` has more than one dimension, the
            function must flatten ``x`` and return the unique elements of
            the flattened array.
    Returns
    *******
    
    *   **out**: *Tuple[ <array>, <array> ]*
    
        *   a namedtuple ``(values, inverse_indices)`` whose
    
            *   first element must have the field name ``values`` and must
                be an array containing the unique elements of ``x``. The
                array must have the same data type as ``x``.
    
            *   second element must have the field name
                ``inverse_indices`` and must be an array containing the
                indices of ``values`` that reconstruct ``x``. The array
                must have the same shape as ``x`` and have the default
                integer data type.
    
            Note: The order of unique elements is not specified and may vary
                between implementations."""
    raise NotImplemented

def unique_values(x, /):
    """Data-dependent output shape: The shape of the output array for this
    function depends on the data values in the input array; hence, array
    libraries which build computation graphs (e.g., JAX, Dask, etc.) may
    find this function difficult to implement without knowing array
    values. Accordingly, such libraries may choose to omit this function.
    See data-dependent-output-shapes section for more details.
    Returns the unique elements of an input array ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. If ``x`` has more than one dimension, the
            function must flatten ``x`` and return the unique elements of
            the flattened array.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the set of unique elements in ``x``. The
            returned array must have the same data type as ``x``.
    
            Note: The order of unique elements is not specified and may vary
                between implementations."""
    raise NotImplemented

