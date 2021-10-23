def max(x, /, *, axis=None, keepdims=False):
    """Calculates the maximum value of the input array ``x``.
    Note: When the number of elements over which to compute the maximum
        value is zero, the maximum value is implementation-defined.
        Specification-compliant libraries may choose to error, return a
        sentinel value (e.g., if ``x`` is a floating-point input array,
        return ``NaN``), or return the minimum possible value for the
        input array ``x`` data type (e.g., if ``x`` is a floating-point
        array, return ``-infinity``).
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    
    *   **axis**: *Optional[ Union[ int, Tuple[ int, … ] ] ]*
    
        *   axis or axes along which maximum values must be computed. By
            default, the maximum value must be computed over the entire
            array. If a tuple of integers, maximum values must be computed
            over multiple axes. Default: ``None``.
    
    *   **keepdims**: *bool*
    
        *   If ``True``, the reduced axes (dimensions) must be included in
            the result as singleton dimensions, and, accordingly, the
            result must be compatible with the input array (see
            `Broadcasting <#broadcasting>`_). Otherwise, if ``False``, the
            reduced axes (dimensions) must not be included in the result.
            Default: ``False``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   if the maximum value was computed over the entire array, a
            zero-dimensional array containing the maximum value;
            otherwise, a non-zero-dimensional array containing the maximum
            values. The returned array must have the same data type as
            ``x``."""
    raise NotImplemented

def mean(x, /, *, axis=None, keepdims=False):
    """Calculates the arithmetic mean of the input array ``x``.
    Special Cases
    *************
    
    For a floating-point input array ``x``, let ``N`` equal the number of
    elements over which to compute the arithmetic mean and
    
    *   if ``N`` is ``0``, the arithmetic mean is ``NaN``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    
    *   **axis**: *Optional[ Union[ int, Tuple[ int, … ] ] ]*
    
        *   axis or axes along which arithmetic means must be computed. By
            default, the mean must be computed over the entire array. If a
            tuple of integers, arithmetic means must be computed over
            multiple axes. Default: ``None``.
    
    *   **keepdims**: *bool*
    
        *   If ``True``, the reduced axes (dimensions) must be included in
            the result as singleton dimensions, and, accordingly, the
            result must be compatible with the input array (see
            `Broadcasting <#broadcasting>`_). Otherwise, if ``False``, the
            reduced axes (dimensions) must not be included in the result.
            Default: ``False``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   if the arithmetic mean was computed over the entire array, a
            zero-dimensional array containing the arithmetic mean;
            otherwise, a non-zero-dimensional array containing the
            arithmetic means. The returned array must have the same data
            type as ``x``.
    
            Note: While this specification recommends that this function
                only accept input arrays having a floating-point data
                type, specification-compliant array libraries may choose
                to accept input arrays having an integer data type. While
                mixed data type promotion is implementation-defined, if
                the input array ``x`` has an integer data type, the
                returned array must have the default floating-point data
                type."""
    raise NotImplemented

def min(x, /, *, axis=None, keepdims=False):
    """Calculates the minimum value of the input array ``x``.
    Note: When the number of elements over which to compute the minimum
        value is zero, the minimum value is implementation-defined.
        Specification-compliant libraries may choose to error, return a
        sentinel value (e.g., if ``x`` is a floating-point input array,
        return ``NaN``), or return the maximum possible value for the
        input array ``x`` data type (e.g., if ``x`` is a floating-point
        array, return ``+infinity``).
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    
    *   **axis**: *Optional[ Union[ int, Tuple[ int, … ] ] ]*
    
        *   axis or axes along which minimum values must be computed. By
            default, the minimum value must be computed over the entire
            array. If a tuple of integers, minimum values must be computed
            over multiple axes. Default: ``None``.
    
    *   **keepdims**: *bool*
    
        *   If ``True``, the reduced axes (dimensions) must be included in
            the result as singleton dimensions, and, accordingly, the
            result must be compatible with the input array (see
            `Broadcasting <#broadcasting>`_). Otherwise, if ``False``, the
            reduced axes (dimensions) must not be included in the result.
            Default: ``False``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   if the minimum value was computed over the entire array, a
            zero-dimensional array containing the minimum value;
            otherwise, a non-zero-dimensional array containing the minimum
            values. The returned array must have the same data type as
            ``x``."""
    raise NotImplemented

def prod(x, /, *, axis=None, dtype=None, keepdims=False):
    """Calculates the product of input array ``x`` elements.
    Special Cases
    *************
    
    For an input array ``x``, let ``N`` equal the number of elements over
    which to compute the product and
    
    *   if ``N`` is ``0``, the product is ``1`` (i.e., the empty product).
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    
    *   **axis**: *Optional[ Union[ int, Tuple[ int, … ] ] ]*
    
        *   axis or axes along which products must be computed. By
            default, the product must be computed over the entire array.
            If a tuple of integers, products must be computed over
            multiple axes. Default: ``None``.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   data type of the returned array. If ``None``,
    
            *   if the default data type corresponding to the data type
                “kind” (integer or floating-point) of ``x`` has a smaller
                range of values than the data type of ``x`` (e.g., ``x``
                has data type ``int64`` and the default data type is
                ``int32``, or ``x`` has data type ``uint64`` and the
                default data type is ``int64``), the returned array must
                have the same data type as ``x``.
    
            *   otherwise, the returned array must have the default data
                type corresponding to the data type “kind” (integer or
                floating-point) of ``x``.
    
            If the data type (either specified or resolved) differs from
            the data type of ``x``, the input array should be cast to the
            specified data type before computing the product. Default:
            ``None``.
    
            Note: This keyword argument is intended to help prevent data
                type overflows.
    
    *   **keepdims**: *bool*
    
        *   If ``True``, the reduced axes (dimensions) must be included in
            the result as singleton dimensions, and, accordingly, the
            result must be compatible with the input array (see
            `Broadcasting <#broadcasting>`_). Otherwise, if ``False``, the
            reduced axes (dimensions) must not be included in the result.
            Default: ``False``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   if the product was computed over the entire array, a
            zero-dimensional array containing the product; otherwise, a
            non-zero-dimensional array containing the products. The
            returned array must have a data type as described by the
            ``dtype`` parameter above."""
    raise NotImplemented

def std(x, /, *, axis=None, correction=0.0, keepdims=False):
    """Calculates the standard deviation of the input array ``x``.
    Special Cases
    *************
    
    For a floating-point input array ``x``, let ``N`` equal the number of
    elements over which to compute the standard deviation and
    
    *   if ``N - correction`` is less than or equal to ``0``, the standard
        deviation is ``NaN``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    
    *   **axis**: *Optional[ Union[ int, Tuple[ int, … ] ] ]*
    
        *   axis or axes along which standard deviations must be computed.
            By default, the standard deviation must be computed over the
            entire array. If a tuple of integers, standard deviations must
            be computed over multiple axes. Default: ``None``.
    
    *   **correction**: *Union[ int, float ]*
    
        *   degrees of freedom adjustment. Setting this parameter to a
            value other than ``0`` has the effect of adjusting the divisor
            during the calculation of the standard deviation according to
            ``N-c`` where ``N`` corresponds to the total number of
            elements over which the standard deviation is computed and
            ``c`` corresponds to the provided degrees of freedom
            adjustment. When computing the standard deviation of a
            population, setting this parameter to ``0`` is the standard
            choice (i.e., the provided array contains data constituting an
            entire population). When computing the corrected sample
            standard deviation, setting this parameter to ``1`` is the
            standard choice (i.e., the provided array contains data
            sampled from a larger population; this is commonly referred to
            as Bessel’s correction). Default: ``0``.
    
    *   **keepdims**: *bool*
    
        *   If ``True``, the reduced axes (dimensions) must be included in
            the result as singleton dimensions, and, accordingly, the
            result must be compatible with the input array (see
            `Broadcasting <#broadcasting>`_). Otherwise, if ``False``, the
            reduced axes (dimensions) must not be included in the result.
            Default: ``False``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   if the standard deviation was computed over the entire array,
            a zero-dimensional array containing the standard deviation;
            otherwise, a non-zero-dimensional array containing the
            standard deviations. The returned array must have the same
            data type as ``x``.
    
            Note: While this specification recommends that this function
                only accept input arrays having a floating-point data
                type, specification-compliant array libraries may choose
                to accept input arrays having an integer data type. While
                mixed data type promotion is implementation-defined, if
                the input array ``x`` has an integer data type, the
                returned array must have the default floating-point data
                type."""
    raise NotImplemented

def sum(x, /, *, axis=None, dtype=None, keepdims=False):
    """Calculates the sum of the input array ``x``.
    Special Cases
    *************
    
    For an input array ``x``, let ``N`` equal the number of elements over
    which to compute the sum and
    
    *   if ``N`` is ``0``, the sum is ``0`` (i.e., the empty sum).
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a numeric data type.
    
    *   **axis**: *Optional[ Union[ int, Tuple[ int, … ] ] ]*
    
        *   axis or axes along which sums must be computed. By default,
            the sum must be computed over the entire array. If a tuple of
            integers, sums must be computed over multiple axes. Default:
            ``None``.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   data type of the returned array. If ``None``,
    
            *   if the default data type corresponding to the data type
                “kind” (integer or floating-point) of ``x`` has a smaller
                range of values than the data type of ``x`` (e.g., ``x``
                has data type ``int64`` and the default data type is
                ``int32``, or ``x`` has data type ``uint64`` and the
                default data type is ``int64``), the returned array must
                have the same data type as ``x``.
    
            *   otherwise, the returned array must have the default data
                type corresponding to the data type “kind” (integer or
                floating-point) of ``x``.
    
            If the data type (either specified or resolved) differs from
            the data type of ``x``, the input array should be cast to the
            specified data type before computing the sum. Default:
            ``None``.
    
            Note: This keyword argument is intended to help prevent data
                type overflows.
    
    *   **keepdims**: *bool*
    
        *   If ``True``, the reduced axes (dimensions) must be included in
            the result as singleton dimensions, and, accordingly, the
            result must be compatible with the input array (see
            `Broadcasting <#broadcasting>`_). Otherwise, if ``False``, the
            reduced axes (dimensions) must not be included in the result.
            Default: ``False``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   if the sum was computed over the entire array, a
            zero-dimensional array containing the sum; otherwise, an array
            containing the sums. The returned array must have a data type
            as described by the ``dtype`` parameter above."""
    raise NotImplemented

def var(x, /, *, axis=None, correction=0.0, keepdims=False):
    """Calculates the variance of the input array ``x``.
    Special Cases
    *************
    
    For a floating-point input array ``x``, let ``N`` equal the number of
    elements over which to compute the variance and
    
    *   if ``N - correction`` is less than or equal to ``0``, the variance
        is ``NaN``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array. Should have a floating-point data type.
    
    *   **axis**: *Optional[ Union[ int, Tuple[ int, … ] ] ]*
    
        *   axis or axes along which variances must be computed. By
            default, the variance must be computed over the entire array.
            If a tuple of integers, variances must be computed over
            multiple axes. Default: ``None``.
    
    *   **correction**: *Union[ int, float ]*
    
        *   degrees of freedom adjustment. Setting this parameter to a
            value other than ``0`` has the effect of adjusting the divisor
            during the calculation of the variance according to ``N-c``
            where ``N`` corresponds to the total number of elements over
            which the variance is computed and ``c`` corresponds to the
            provided degrees of freedom adjustment. When computing the
            variance of a population, setting this parameter to ``0`` is
            the standard choice (i.e., the provided array contains data
            constituting an entire population). When computing the
            unbiased sample variance, setting this parameter to ``1`` is
            the standard choice (i.e., the provided array contains data
            sampled from a larger population; this is commonly referred to
            as Bessel’s correction). Default: ``0``.
    
    *   **keepdims**: *bool*
    
        *   If ``True``, the reduced axes (dimensions) must be included in
            the result as singleton dimensions, and, accordingly, the
            result must be compatible with the input array (see
            `Broadcasting <#broadcasting>`_). Otherwise, if ``False``, the
            reduced axes (dimensions) must not be included in the result.
            Default: ``False``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   if the variance was computed over the entire array, a
            zero-dimensional array containing the variance; otherwise, a
            non-zero-dimensional array containing the variances. The
            returned array must have the same data type as ``x``.
    
            Note: While this specification recommends that this function
                only accept input arrays having a floating-point data
                type, specification-compliant array libraries may choose
                to accept input arrays having an integer data type. While
                mixed data type promotion is implementation-defined, if
                the input array ``x`` has an integer data type, the
                returned array must have the default floating-point data
                type."""
    raise NotImplemented

