def abs(x, /):
    """Calculates the absolute value for each element ``x_i`` of the input
    array ``x`` (i.e., the element-wise result has the same magnitude as
    the respective element in ``x`` but has positive sign).
    Note: For signed integer data types, the absolute value of the minimum
        representable integer is implementation-dependent.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``-0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-infinity``, the result is ``+infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the absolute value of each element in
            ``x``. The returned array must have the same data type as
            ``x``."""
    raise NotImplementedError

def acos(x, /):
    """Calculates an implementation-dependent approximation of the principal
    value of the inverse cosine, having domain ``[-1, +1]`` and codomain
    ``[+0, +π]``, for each element ``x_i`` of the input array ``x``. Each
    element-wise result is expressed in radians.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is greater than ``1``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``-1``, the result is ``NaN``.
    
    *   If ``x_i`` is ``1``, the result is ``+0``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the inverse cosine of each element in
            ``x``. The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def acosh(x, /):
    """Calculates an implementation-dependent approximation to the inverse
    hyperbolic cosine, having domain ``[+1, +infinity]`` and codomain
    ``[+0, +infinity]``, for each element ``x_i`` of the input array
    ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``1``, the result is ``NaN``.
    
    *   If ``x_i`` is ``1``, the result is ``+0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements each represent the area of a
            hyperbolic sector. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the inverse hyperbolic cosine of each
            element in ``x``. The returned array must have a
            floating-point data type determined by `Type Promotion Rules
            <#type-promotion>`_."""
    raise NotImplementedError

def add(x1, x2, /):
    """Calculates the sum for each element ``x1_i`` of the input array ``x1``
    with the respective element ``x2_i`` of the input array ``x2``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``-infinity``, the
        result is ``NaN``.
    
    *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``+infinity``, the
        result is ``NaN``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``+infinity``, the
        result is ``+infinity``.
    
    *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``-infinity``, the
        result is ``-infinity``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is a finite number, the
        result is ``+infinity``.
    
    *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is a finite number, the
        result is ``-infinity``.
    
    *   If ``x1_i`` is a finite number and ``x2_i`` is ``+infinity``, the
        result is ``+infinity``.
    
    *   If ``x1_i`` is a finite number and ``x2_i`` is ``-infinity``, the
        result is ``-infinity``.
    
    *   If ``x1_i`` is ``-0`` and ``x2_i`` is ``-0``, the result is
        ``-0``.
    
    *   If ``x1_i`` is ``-0`` and ``x2_i`` is ``+0``, the result is
        ``+0``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is ``-0``, the result is
        ``+0``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is ``+0``, the result is
        ``+0``.
    
    *   If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is a nonzero
        finite number, the result is ``x2_i``.
    
    *   If ``x1_i`` is a nonzero finite number and ``x2_i`` is either
        ``+0`` or ``-0``, the result is ``x1_i``.
    
    *   If ``x1_i`` is a nonzero finite number and ``x2_i`` is ``-x1_i``,
        the result is ``+0``.
    
    *   In the remaining cases, when neither ``infinity``, ``+0``, ``-0``,
        nor a ``NaN`` is involved, and the operands have the same
        mathematical sign or have different magnitudes, the sum must be
        computed and rounded to the nearest representable value according
        to IEEE 754-2019 and a supported round mode. If the magnitude is
        too large to represent, the operation overflows and the result is
        an ``infinity`` of appropriate mathematical sign.
    
    Note: Floating-point addition is a commutative operation, but not always
        associative.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise sums. The returned array
            must have a data type determined by `Type Promotion Rules
            <#type-promotion>`_."""
    raise NotImplementedError

def asin(x, /):
    """Calculates an implementation-dependent approximation of the principal
    value of the inverse sine, having domain ``[-1, +1]`` and codomain
    ``[-π/2, +π/2]`` for each element ``x_i`` of the input array ``x``.
    Each element-wise result is expressed in radians.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is greater than ``1``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``-1``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the inverse sine of each element in ``x``.
            The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def asinh(x, /):
    """Calculates an implementation-dependent approximation to the inverse
    hyperbolic sine, having domain ``[-infinity, +infinity]`` and codomain
    ``[-infinity, +infinity]``, for each element ``x_i`` in the input
    array ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    
    *   If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements each represent the area of a
            hyperbolic sector. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the inverse hyperbolic sine of each
            element in ``x``. The returned array must have a
            floating-point data type determined by `Type Promotion Rules
            <#type-promotion>`_."""
    raise NotImplementedError

def atan(x, /):
    """Calculates an implementation-dependent approximation of the principal
    value of the inverse tangent, having domain ``[-infinity, +infinity]``
    and codomain ``[-π/2, +π/2]``, for each element ``x_i`` of the input
    array ``x``. Each element-wise result is expressed in radians.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is ``+infinity``, the result is an
        implementation-dependent approximation to ``+π/2``.
    
    *   If ``x_i`` is ``-infinity``, the result is an
        implementation-dependent approximation to ``-π/2``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the inverse tangent of each element in
            ``x``. The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def atan2(x1, x2, /):
    """Calculates an implementation-dependent approximation of the inverse
    tangent of the quotient ``x1/x2``, having domain ``[-infinity,
    +infinity] x [-infinity, +infinity]`` (where the ``x`` notation
    denotes the set of ordered pairs of elements ``(x1_i, x2_i)``) and
    codomain ``[-π, +π]``, for each pair of elements ``(x1_i, x2_i)`` of
    the input arrays ``x1`` and ``x2``, respectively. Each element-wise
    result is expressed in radians.
    The mathematical signs of ``x1_i`` and ``x2_i`` determine the quadrant
    of each element-wise result. The quadrant (i.e., branch) is chosen
    such that each element-wise result is the signed angle in radians
    between the ray ending at the origin and passing through the point
    ``(1,0)`` and the ray ending at the origin and passing through the
    point ``(x2_i, x1_i)``.
    Note: Note the role reversal: the “y-coordinate” is the first function
        parameter; the “x-coordinate” is the second function parameter.
        The parameter order is intentional and traditional for the
        two-argument inverse tangent function where the y-coordinate
        argument is first and the x-coordinate argument is second.
    By IEEE 754 convention, the inverse tangent of the quotient ``x1/x2``
    is defined for ``x2_i`` equal to positive or negative zero and for
    either or both of ``x1_i`` and ``x2_i`` equal to positive or negative
    ``infinity``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the
        result is an implementation-dependent approximation to ``+π/2``.
    
    *   If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the
        result is an implementation-dependent approximation to ``+π/2``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the
        result is ``+0``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is ``+0``, the result is
        ``+0``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is ``-0``, the result is an
        implementation-dependent approximation to ``+π``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result
        is an implementation-dependent approximation to ``+π``.
    
    *   If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the
        result is ``-0``.
    
    *   If ``x1_i`` is ``-0`` and ``x2_i`` is ``+0``, the result is
        ``-0``.
    
    *   If ``x1_i`` is ``-0`` and ``x2_i`` is ``-0``, the result is an
        implementation-dependent approximation to ``-π``.
    
    *   If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result
        is an implementation-dependent approximation to ``-π``.
    
    *   If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result
        is an implementation-dependent approximation to ``-π/2``.
    
    *   If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result
        is an implementation-dependent approximation to ``-π/2``.
    
    *   If ``x1_i`` is greater than ``0``, ``x1_i`` is a finite number,
        and ``x2_i`` is ``+infinity``, the result is ``+0``.
    
    *   If ``x1_i`` is greater than ``0``, ``x1_i`` is a finite number,
        and ``x2_i`` is ``-infinity``, the result is an
        implementation-dependent approximation to ``+π``.
    
    *   If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number, and
        ``x2_i`` is ``+infinity``, the result is ``-0``.
    
    *   If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number, and
        ``x2_i`` is ``-infinity``, the result is an
        implementation-dependent approximation to ``-π``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is finite, the result is
        an implementation-dependent approximation to ``+π/2``.
    
    *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is finite, the result is
        an implementation-dependent approximation to ``-π/2``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``+infinity``, the
        result is an implementation-dependent approximation to ``+π/4``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``-infinity``, the
        result is an implementation-dependent approximation to ``+3π/4``.
    
    *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``+infinity``, the
        result is an implementation-dependent approximation to ``-π/4``.
    
    *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``-infinity``, the
        result is an implementation-dependent approximation to ``-3π/4``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   input array corresponding to the y-coordinates. Should have a
            floating-point data type.
    
    *   **x2**: *<array>*
    
        *   input array corresponding to the x-coordinates. Must be
            compatible with ``x1`` (see `Broadcasting <#broadcasting>`_).
            Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the inverse tangent of the quotient
            ``x1/x2``. The returned array must have a floating-point data
            type determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def atanh(x, /):
    """Calculates an implementation-dependent approximation to the inverse
    hyperbolic tangent, having domain ``[-1, +1]`` and codomain
    ``[-infinity, +infinity]``, for each element ``x_i`` of the input
    array ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``-1``, the result is ``NaN``.
    
    *   If ``x_i`` is greater than ``1``, the result is ``NaN``.
    
    *   If ``x_i`` is ``-1``, the result is ``-infinity``.
    
    *   If ``x_i`` is ``+1``, the result is ``+infinity``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements each represent the area of a
            hyperbolic sector. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the inverse hyperbolic tangent of each
            element in ``x``. The returned array must have a
            floating-point data type determined by `Type Promotion Rules
            <#type-promotion>`_."""
    raise NotImplementedError

def bitwise_and(x1, x2, /):
    """Computes the bitwise AND of the underlying binary representation of
    each element ``x1_i`` of the input array ``x1`` with the respective
    element ``x2_i`` of the input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have an integer or boolean data
            type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have an integer or
            boolean data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def bitwise_left_shift(x1, x2, /):
    """Shifts the bits of each element ``x1_i`` of the input array ``x1`` to
    the left by appending ``x2_i`` (i.e., the respective element in the
    input array ``x2``) zeros to the right of ``x1_i``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have an integer data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have an integer data
            type. Each element must be greater than or equal to ``0``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def bitwise_invert(x, /):
    """Inverts (flips) each bit for each element ``x_i`` of the input array
    ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have an integer or boolean data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have the same data type as ``x``."""
    raise NotImplementedError

def bitwise_or(x1, x2, /):
    """Computes the bitwise OR of the underlying binary representation of
    each element ``x1_i`` of the input array ``x1`` with the respective
    element ``x2_i`` of the input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have an integer or boolean data
            type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have an integer or
            boolean data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def bitwise_right_shift(x1, x2, /):
    """Shifts the bits of each element ``x1_i`` of the input array ``x1`` to
    the right according to the respective element ``x2_i`` of the input
    array ``x2``.
    Note: This operation must be an arithmetic shift (i.e.,
        sign-propagating) and thus equivalent to floor division by a power
        of two.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have an integer data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have an integer data
            type. Each element must be greater than or equal to ``0``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def bitwise_xor(x1, x2, /):
    """Computes the bitwise XOR of the underlying binary representation of
    each element ``x1_i`` of the input array ``x1`` with the respective
    element ``x2_i`` of the input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have an integer or boolean data
            type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have an integer or
            boolean data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def ceil(x, /):
    """Rounds each element ``x_i`` of the input array ``x`` to the smallest
    (i.e., closest to ``-infinity``) integer-valued number that is not
    less than ``x_i``.
    Special Cases
    *************
    
    *   If ``x_i`` is already integer-valued, the result is ``x_i``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the rounded result for each element in
            ``x``. The returned array must have the same data type as
            ``x``."""
    raise NotImplementedError

def cos(x, /):
    """Calculates an implementation-dependent approximation to the cosine,
    having domain ``(-infinity, +infinity)`` and codomain ``[-1, +1]``,
    for each element ``x_i`` of the input array ``x``. Each element
    ``x_i`` is assumed to be expressed in radians.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``1``.
    
    *   If ``x_i`` is ``-0``, the result is ``1``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``NaN``.
    
    *   If ``x_i`` is ``-infinity``, the result is ``NaN``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements are each expressed in radians.
            Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the cosine of each element in ``x``. The
            returned array must have a floating-point data type determined
            by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def cosh(x, /):
    """Calculates an implementation-dependent approximation to the hyperbolic
    cosine, having domain ``[-infinity, +infinity]`` and codomain
    ``[-infinity, +infinity]``, for each element ``x_i`` in the input
    array ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``1``.
    
    *   If ``x_i`` is ``-0``, the result is ``1``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    
    *   If ``x_i`` is ``-infinity``, the result is ``+infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements each represent a hyperbolic angle.
            Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the hyperbolic cosine of each element in
            ``x``. The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def divide(x1, x2, /):
    """Calculates the division for each element ``x1_i`` of the input array
    ``x1`` with the respective element ``x2_i`` of the input array ``x2``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i``
        is either ``+infinity`` or ``-infinity``, the result is ``NaN``.
    
    *   If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either
        ``+0`` or ``-0``, the result is ``NaN``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the
        result is ``+0``.
    
    *   If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the
        result is ``-0``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result
        is ``-0``.
    
    *   If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result
        is ``+0``.
    
    *   If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the
        result is ``+infinity``.
    
    *   If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the
        result is ``-infinity``.
    
    *   If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result
        is ``-infinity``.
    
    *   If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result
        is ``+infinity``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is a positive (i.e.,
        greater than ``0``) finite number, the result is ``+infinity``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is a negative (i.e.,
        less than ``0``) finite number, the result is ``-infinity``.
    
    *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is a positive (i.e.,
        greater than ``0``) finite number, the result is ``-infinity``.
    
    *   If ``x1_i`` is ``-infinity`` and ``x2_i`` is a negative (i.e.,
        less than ``0``) finite number, the result is ``+infinity``.
    
    *   If ``x1_i`` is a positive (i.e., greater than ``0``) finite number
        and ``x2_i`` is ``+infinity``, the result is ``+0``.
    
    *   If ``x1_i`` is a positive (i.e., greater than ``0``) finite number
        and ``x2_i`` is ``-infinity``, the result is ``-0``.
    
    *   If ``x1_i`` is a negative (i.e., less than ``0``) finite number
        and ``x2_i`` is ``+infinity``, the result is ``-0``.
    
    *   If ``x1_i`` is a negative (i.e., less than ``0``) finite number
        and ``x2_i`` is ``-infinity``, the result is ``+0``.
    
    *   If ``x1_i`` and ``x2_i`` have the same mathematical sign and are
        both nonzero finite numbers, the result has a positive
        mathematical sign.
    
    *   If ``x1_i`` and ``x2_i`` have different mathematical signs and are
        both nonzero finite numbers, the result has a negative
        mathematical sign.
    
    *   In the remaining cases, where neither ``-infinity``, ``+0``,
        ``-0``, nor ``NaN`` is involved, the quotient must be computed and
        rounded to the nearest representable value according to IEEE
        754-2019 and a supported rounding mode. If the magnitude is too
        larger to represent, the operation overflows and the result is an
        ``infinity`` of appropriate mathematical sign. If the magnitude is
        too small to represent, the operation underflows and the result is
        a zero of appropriate mathematical sign.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   dividend input array. Should have a floating-point data type.
    
    *   **x2**: *<array>*
    
        *   divisor input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a floating-point
            data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a floating-point data type determined by `Type
            Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def equal(x1, x2, /):
    """Computes the truth value of ``x1_i == x2_i`` for each element ``x1_i``
    of the input array ``x1`` with the respective element ``x2_i`` of the
    input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. May have any data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). May have any data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def exp(x, /):
    """Calculates an implementation-dependent approximation to the
    exponential function, having domain ``[-infinity, +infinity]`` and
    codomain ``[+0, +infinity]``, for each element ``x_i`` of the input
    array ``x`` (``e`` raised to the power of ``x_i``, where ``e`` is the
    base of the natural logarithm).
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``1``.
    
    *   If ``x_i`` is ``-0``, the result is ``1``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    
    *   If ``x_i`` is ``-infinity``, the result is ``+0``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated exponential function result
            for each element in ``x``. The returned array must have a
            floating-point data type determined by `Type Promotion Rules
            <#type-promotion>`_."""
    raise NotImplementedError

def expm1(x, /):
    """Calculates an implementation-dependent approximation to ``exp(x)-1``,
    having domain ``[-infinity, +infinity]`` and codomain ``[-1,
    +infinity]``, for each element ``x_i`` of the input array ``x``.
    Note: The purpose of this function is to calculate ``exp(x)-1.0`` more
        accurately when ``x`` is close to zero. Accordingly, conforming
        implementations should avoid implementing this function as simply
        ``exp(x)-1.0``. See FDLIBM, or some other IEEE 754-2019 compliant
        mathematical library, for a potential reference implementation.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    
    *   If ``x_i`` is ``-infinity``, the result is ``-1``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated result for each element in
            ``x``. The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def floor(x, /):
    """Rounds each element ``x_i`` of the input array ``x`` to the greatest
    (i.e., closest to ``+infinity``) integer-valued number that is not
    greater than ``x_i``.
    Special Cases
    *************
    
    *   If ``x_i`` is already integer-valued, the result is ``x_i``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the rounded result for each element in
            ``x``. The returned array must have the same data type as
            ``x``."""
    raise NotImplementedError

def floor_divide(x1, x2, /):
    """Rounds the result of dividing each element ``x1_i`` of the input array
    ``x1`` by the respective element ``x2_i`` of the input array ``x2`` to
    the greatest (i.e., closest to ``+infinity``) integer-value number
    that is not greater than the division result.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   dividend input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   divisor input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def greater(x1, x2, /):
    """Computes the truth value of ``x1_i > x2_i`` for each element ``x1_i``
    of the input array ``x1`` with the respective element ``x2_i`` of the
    input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def greater_equal(x1, x2, /):
    """Computes the truth value of ``x1_i >= x2_i`` for each element ``x1_i``
    of the input array ``x1`` with the respective element ``x2_i`` of the
    input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def isfinite(x, /):
    """Tests each element ``x_i`` of the input array ``x`` to determine if
    finite (i.e., not ``NaN`` and not equal to positive or negative
    infinity).
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing test results. An element ``out_i`` is
            ``True`` if ``x_i`` is finite and ``False`` otherwise. The
            returned array must have a data type of ``bool``."""
    raise NotImplementedError

def isinf(x, /):
    """Tests each element ``x_i`` of the input array ``x`` to determine if
    equal to positive or negative infinity.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing test results. An element ``out_i`` is
            ``True`` if ``x_i`` is either positive or negative infinity
            and ``False`` otherwise. The returned array must have a data
            type of ``bool``."""
    raise NotImplementedError

def isnan(x, /):
    """Tests each element ``x_i`` of the input array ``x`` to determine
    whether the element is ``NaN``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing test results. An element ``out_i`` is
            ``True`` if ``x_i`` is ``NaN`` and ``False`` otherwise. The
            returned array should have a data type of ``bool``."""
    raise NotImplementedError

def less(x1, x2, /):
    """Computes the truth value of ``x1_i < x2_i`` for each element ``x1_i``
    of the input array ``x1`` with the respective element ``x2_i`` of the
    input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def less_equal(x1, x2, /):
    """Computes the truth value of ``x1_i <= x2_i`` for each element ``x1_i``
    of the input array ``x1`` with the respective element ``x2_i`` of the
    input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def log(x, /):
    """Calculates an implementation-dependent approximation to the natural
    (base ``e``) logarithm, having domain ``[0, +infinity]`` and codomain
    ``[-infinity, +infinity]``, for each element ``x_i`` of the input
    array ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``0``, the result is ``NaN``.
    
    *   If ``x_i`` is either ``+0`` or ``-0``, the result is
        ``-infinity``.
    
    *   If ``x_i`` is ``1``, the result is ``+0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated natural logarithm for each
            element in ``x``. The returned array must have a
            floating-point data type determined by `Type Promotion Rules
            <#type-promotion>`_."""
    raise NotImplementedError

def log1p(x, /):
    """Calculates an implementation-dependent approximation to ``log(1+x)``,
    where ``log`` refers to the natural (base ``e``) logarithm, having
    domain ``[-1, +infinity]`` and codomain ``[-infinity, +infinity]``,
    for each element ``x_i`` of the input array ``x``.
    Note: The purpose of this function is to calculate ``log(1+x)`` more
        accurately when ``x`` is close to zero. Accordingly, conforming
        implementations should avoid implementing this function as simply
        ``log(1+x)``. See FDLIBM, or some other IEEE 754-2019 compliant
        mathematical library, for a potential reference implementation.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``-1``, the result is ``NaN``.
    
    *   If ``x_i`` is ``-1``, the result is ``-infinity``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated result for each element in
            ``x``. The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def log2(x, /):
    """Calculates an implementation-dependent approximation to the base ``2``
    logarithm, having domain ``[0, +infinity]`` and codomain ``[-infinity,
    +infinity]``, for each element ``x_i`` of the input array ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``0``, the result is ``NaN``.
    
    *   If ``x_i`` is either ``+0`` or ``-0``, the result is
        ``-infinity``.
    
    *   If ``x_i`` is ``1``, the result is ``+0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated base ``2`` logarithm for
            each element in ``x``. The returned array must have a
            floating-point data type determined by `Type Promotion Rules
            <#type-promotion>`_."""
    raise NotImplementedError

def log10(x, /):
    """Calculates an implementation-dependent approximation to the base
    ``10`` logarithm, having domain ``[0, +infinity]`` and codomain
    ``[-infinity, +infinity]``, for each element ``x_i`` of the input
    array ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``0``, the result is ``NaN``.
    
    *   If ``x_i`` is either ``+0`` or ``-0``, the result is
        ``-infinity``.
    
    *   If ``x_i`` is ``1``, the result is ``+0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated base ``10`` logarithm for
            each element in ``x``. The returned array must have a
            floating-point data type determined by `Type Promotion Rules
            <#type-promotion>`_."""
    raise NotImplementedError

def logaddexp(x1, x2):
    """Calculates the logarithm of the sum of exponentiations ``log(exp(x1) +
    exp(x2))`` for each element ``x1_i`` of the input array ``x1`` with
    the respective element ``x2_i`` of the input array ``x2``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is not ``NaN``, the
        result is ``+infinity``.
    
    *   If ``x1_i`` is not ``NaN`` and ``x2_i`` is ``+infinity``, the
        result is ``+infinity``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a floating-point data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a floating-point
            data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a floating-point data type determined by `Type
            Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def logical_and(x1, x2, /):
    """Computes the logical AND for each element ``x1_i`` of the input array
    ``x1`` with the respective element ``x2_i`` of the input array ``x2``.
    Note: While this specification recommends that this function only accept
        input arrays having a boolean data type, specification-compliant
        array libraries may choose to accept input arrays having numeric
        data types. If non-boolean data types are supported, zeros must be
        considered the equivalent of ``False``, while non-zeros must be
        considered the equivalent of ``True``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a boolean data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a boolean data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def logical_not(x, /):
    """Computes the logical NOT for each element ``x_i`` of the input array
    ``x``.
    Note: While this specification recommends that this function only accept
        input arrays having a boolean data type, specification-compliant
        array libraries may choose to accept input arrays having numeric
        data types. If non-boolean data types are supported, zeros must be
        considered the equivalent of ``False``, while non-zeros must be
        considered the equivalent of ``True``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a boolean data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def logical_or(x1, x2, /):
    """Computes the logical OR for each element ``x1_i`` of the input array
    ``x1`` with the respective element ``x2_i`` of the input array ``x2``.
    Note: While this specification recommends that this function only accept
        input arrays having a boolean data type, specification-compliant
        array libraries may choose to accept input arrays having numeric
        data types. If non-boolean data types are supported, zeros must be
        considered the equivalent of ``False``, while non-zeros must be
        considered the equivalent of ``True``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a boolean data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a boolean data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def logical_xor(x1, x2, /):
    """Computes the logical XOR for each element ``x1_i`` of the input array
    ``x1`` with the respective element ``x2_i`` of the input array ``x2``.
    Note: While this specification recommends that this function only accept
        input arrays having a boolean data type, specification-compliant
        array libraries may choose to accept input arrays having numeric
        data types. If non-boolean data types are supported, zeros must be
        considered the equivalent of ``False``, while non-zeros must be
        considered the equivalent of ``True``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a boolean data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a boolean data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def multiply(x1, x2, /):
    """Calculates the product for each element ``x1_i`` of the input array
    ``x1`` with the respective element ``x2_i`` of the input array ``x2``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i``
        is either ``+0`` or ``-0``, the result is ``NaN``.
    
    *   If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either
        ``+infinity`` or ``-infinity``, the result is ``NaN``.
    
    *   If ``x1_i`` and ``x2_i`` have the same mathematical sign, the
        result has a positive mathematical sign, unless the result is
        ``NaN``. If the result is ``NaN``, the “sign” of ``NaN`` is
        implementation-defined.
    
    *   If ``x1_i`` and ``x2_i`` have different mathematical signs, the
        result has a negative mathematical sign, unless the result is
        ``NaN``. If the result is ``NaN``, the “sign” of ``NaN`` is
        implementation-defined.
    
    *   If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i``
        is either ``+infinity`` or ``-infinity``, the result is a signed
        infinity with the mathematical sign determined by the rule already
        stated above.
    
    *   If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i``
        is a nonzero finite number, the result is a signed infinity with
        the mathematical sign determined by the rule already stated above.
    
    *   If ``x1_i`` is a nonzero finite number and ``x2_i`` is either
        ``+infinity`` or ``-infinity``, the result is a signed infinity
        with the mathematical sign determined by the rule already stated
        above.
    
    *   In the remaining cases, where neither ``infinity`` nor ``NaN`` is
        involved, the product must be computed and rounded to the nearest
        representable value according to IEEE 754-2019 and a supported
        rounding mode. If the magnitude is too large to represent, the
        result is an ``infinity`` of appropriate mathematical sign. If the
        magnitude is too small to represent, the result is a zero of
        appropriate mathematical sign.
    
    Note: Floating-point multiplication is not always associative due to
        finite precision.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise products. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def negative(x, /):
    """Computes the numerical negative of each element ``x_i`` (i.e., ``y_i =
    -x_i``) of the input array ``x``.
    Note: For signed integer data types, the numerical negative of the
        minimum representable integer is implementation-dependent.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated result for each element in
            ``x``. The returned array must have a data type determined by
            `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def not_equal(x1, x2, /):
    """Computes the truth value of ``x1_i != x2_i`` for each element ``x1_i``
    of the input array ``x1`` with the respective element ``x2_i`` of the
    input array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. May have any data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_).
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type of ``bool``."""
    raise NotImplementedError

def positive(x, /):
    """Computes the numerical positive of each element ``x_i`` (i.e., ``y_i =
    +x_i``) of the input array ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated result for each element in
            ``x``. The returned array must have the same data type as
            ``x``."""
    raise NotImplementedError

def pow(x1, x2, /):
    """Calculates an implementation-dependent approximation of exponentiation
    by raising each element ``x1_i`` (the base) of the input array ``x1``
    to the power of ``x2_i`` (the exponent), where ``x2_i`` is the
    corresponding element of the input array ``x2``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x1_i`` is not equal to ``1`` and ``x2_i`` is ``NaN``, the
        result is ``NaN``.
    
    *   If ``x2_i`` is ``+0``, the result is ``1``, even if ``x1_i`` is
        ``NaN``.
    
    *   If ``x2_i`` is ``-0``, the result is ``1``, even if ``x1_i`` is
        ``NaN``.
    
    *   If ``x1_i`` is ``NaN`` and ``x2_i`` is not equal to ``0``, the
        result is ``NaN``.
    
    *   If ``abs(x1_i)`` is greater than ``1`` and ``x2_i`` is
        ``+infinity``, the result is ``+infinity``.
    
    *   If ``abs(x1_i)`` is greater than ``1`` and ``x2_i`` is
        ``-infinity``, the result is ``+0``.
    
    *   If ``abs(x1_i)`` is ``1`` and ``x2_i`` is ``+infinity``, the
        result is ``1``.
    
    *   If ``abs(x1_i)`` is ``1`` and ``x2_i`` is ``-infinity``, the
        result is ``1``.
    
    *   If ``x1_i`` is ``1`` and ``x2_i`` is not ``NaN``, the result is
        ``1``.
    
    *   If ``abs(x1_i)`` is less than ``1`` and ``x2_i`` is ``+infinity``,
        the result is ``+0``.
    
    *   If ``abs(x1_i)`` is less than ``1`` and ``x2_i`` is ``-infinity``,
        the result is ``+infinity``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is greater than ``0``,
        the result is ``+infinity``.
    
    *   If ``x1_i`` is ``+infinity`` and ``x2_i`` is less than ``0``, the
        result is ``+0``.
    
    *   If ``x1_i`` is ``-infinity``, ``x2_i`` is greater than ``0``, and
        ``x2_i`` is an odd integer value, the result is ``-infinity``.
    
    *   If ``x1_i`` is ``-infinity``, ``x2_i`` is greater than ``0``, and
        ``x2_i`` is not an odd integer value, the result is ``+infinity``.
    
    *   If ``x1_i`` is ``-infinity``, ``x2_i`` is less than ``0``, and
        ``x2_i`` is an odd integer value, the result is ``-0``.
    
    *   If ``x1_i`` is ``-infinity``, ``x2_i`` is less than ``0``, and
        ``x2_i`` is not an odd integer value, the result is ``+0``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the
        result is ``+0``.
    
    *   If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result
        is ``+infinity``.
    
    *   If ``x1_i`` is ``-0``, ``x2_i`` is greater than ``0``, and
        ``x2_i`` is an odd integer value, the result is ``-0``.
    
    *   If ``x1_i`` is ``-0``, ``x2_i`` is greater than ``0``, and
        ``x2_i`` is not an odd integer value, the result is ``+0``.
    
    *   If ``x1_i`` is ``-0``, ``x2_i`` is less than ``0``, and ``x2_i``
        is an odd integer value, the result is ``-infinity``.
    
    *   If ``x1_i`` is ``-0``, ``x2_i`` is less than ``0``, and ``x2_i``
        is not an odd integer value, the result is ``+infinity``.
    
    *   If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number,
        ``x2_i`` is a finite number, and ``x2_i`` is not an integer value,
        the result is ``NaN``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array whose elements correspond to the
            exponentiation base. Should have a floating-point data type.
    
    *   **x2**: *<array>*
    
        *   second input array whose elements correspond to the
            exponentiation exponent. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a floating-point
            data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def remainder(x1, x2, /):
    """Returns the remainder of division for each element ``x1_i`` of the
    input array ``x1`` and the respective element ``x2_i`` of the input
    array ``x2``.
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   dividend input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   divisor input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise results. Each
            element-wise result must have the same sign as the respective
            element ``x2_i``. The returned array must have a data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def round(x, /):
    """Rounds each element ``x_i`` of the input array ``x`` to the nearest
    integer-valued number.
    Special Cases
    *************
    
    *   If ``x_i`` is already integer-valued, the result is ``x_i``.
    
    *   If two integers are equally close to ``x_i``, the result is the
        even integer closest to ``x_i``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the rounded result for each element in
            ``x``. The returned array must have the same data type as
            ``x``."""
    raise NotImplementedError

def sign(x, /):
    """Returns an indication of the sign of a number for each element ``x_i``
    of the input array ``x``.
    Special Cases
    *************
    
    *   If ``x_i`` is less than ``0``, the result is ``-1``.
    
    *   If ``x_i`` is either ``-0`` or ``+0``, the result is ``0``.
    
    *   If ``x_i`` is greater than ``0``, the result is ``+1``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated result for each element in
            ``x``. The returned array must have the same data type as
            ``x``."""
    raise NotImplementedError

def sin(x, /):
    """Calculates an implementation-dependent approximation to the sine,
    having domain ``(-infinity, +infinity)`` and codomain ``[-1, +1]``,
    for each element ``x_i`` of the input array ``x``. Each element
    ``x_i`` is assumed to be expressed in radians.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is either ``+infinity`` or ``-infinity``, the result is
        ``NaN``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements are each expressed in radians.
            Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the sine of each element in ``x``. The
            returned array must have a floating-point data type determined
            by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def sinh(x, /):
    """Calculates an implementation-dependent approximation to the hyperbolic
    sine, having domain ``[-infinity, +infinity]`` and codomain
    ``[-infinity, +infinity]``, for each element ``x_i`` of the input
    array ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    
    *   If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements each represent a hyperbolic angle.
            Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the hyperbolic sine of each element in
            ``x``. The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def square(x, /):
    """Squares (``x_i * x_i``) each element ``x_i`` of the input array ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the evaluated result for each element in
            ``x``. The returned array must have a data type determined by
            `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def sqrt(x, /):
    """Calculates the square root, having domain ``[0, +infinity]`` and
    codomain ``[0, +infinity]``, for each element ``x_i`` of the input
    array ``x``. After rounding, each result must be indistinguishable
    from the infinitely precise result (as required by IEEE 754).
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is less than ``0``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the square root of each element in ``x``.
            The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def subtract(x1, x2, /):
    """Calculates the difference for each element ``x1_i`` of the input array
    ``x1`` with the respective element ``x2_i`` of the input array ``x2``.
    The result of ``x1_i - x2_i`` must be the same as ``x1_i + (-x2_i)``
    and must be governed by the same floating-point rules as addition (see
    `add() <add-x1-x2_>`_).
    Parameters
    **********
    
    *   **x1**: *<array>*
    
        *   first input array. Should have a numeric data type.
    
    *   **x2**: *<array>*
    
        *   second input array. Must be compatible with ``x1`` (see
            `Broadcasting <#broadcasting>`_). Should have a numeric data
            type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the element-wise differences. The returned
            array must have a data type determined by `Type Promotion
            Rules <#type-promotion>`_."""
    raise NotImplementedError

def tan(x, /):
    """Calculates an implementation-dependent approximation to the tangent,
    having domain ``(-infinity, +infinity)`` and codomain ``(-infinity,
    +infinity)``, for each element ``x_i`` of the input array ``x``. Each
    element ``x_i`` is assumed to be expressed in radians.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is either ``+infinity`` or ``-infinity``, the result is
        ``NaN``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements are expressed in radians. Should
            have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the tangent of each element in ``x``. The
            returned array must have a floating-point data type determined
            by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def tanh(x, /):
    """Calculates an implementation-dependent approximation to the hyperbolic
    tangent, having domain ``[-infinity, +infinity]`` and codomain ``[-1,
    +1]``, for each element ``x_i`` of the input array ``x``.
    Special Cases
    *************
    
    For floating-point operands,
    
    *   If ``x_i`` is ``NaN``, the result is ``NaN``.
    
    *   If ``x_i`` is ``+0``, the result is ``+0``.
    
    *   If ``x_i`` is ``-0``, the result is ``-0``.
    
    *   If ``x_i`` is ``+infinity``, the result is ``+1``.
    
    *   If ``x_i`` is ``-infinity``, the result is ``-1``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array whose elements each represent a hyperbolic angle.
            Should have a floating-point data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the hyperbolic tangent of each element in
            ``x``. The returned array must have a floating-point data type
            determined by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def trunc(x, /):
    """Rounds each element ``x_i`` of the input array ``x`` to the
    integer-valued number that is closest to but no greater than ``x_i``.
    Special Cases
    *************
    
    *   If ``x_i`` is already integer-valued, the result is ``x_i``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the rounded result for each element in
            ``x``. The returned array must have the same data type as
            ``x``."""
    raise NotImplementedError

