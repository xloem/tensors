import tensors
from tensors import shape
from tensors._backend import load_all_backends, backends_by_name

load_all_backends()
backends = set(backends_by_name.values())

ROUND_DIGITS = 6

def to_array(tensor):
    # this should probably be a library function, and implemented differently when so
    if len(tensor.shape) == 0:
        return round(float(tensor), ROUND_DIGITS) # jax conversion to python float is not round-trip
    else:
        return [to_array(item) for item in tensor]

def random_array(*shape):
    # this should go in the backends, is a common thing
    import random
    if len(shape) == 0:
        return round(random.random() * 4 - 2, ROUND_DIGITS)
    return [random_array(*shape[1:]) for row in range(shape[0])]

def test_construction():
    a = random_array(3,3)
    for backend in backends:
        t = backend.tensor(a)
        assert to_array(t) == a, f'{backend.name} construction of random {shape(a)}'
        end = 4
        t = backend.arange(end)
        assert to_array(t) == [*range(end)], f'{backend.name} creation of range {end}'

# tensorflow gpu -> jax cpu error, maybe implement something like array api device standard
#def test_conversion():
#    a = random_array(3,3)
#    for backend1 in backends:
#        t1 = backend1.tensor(a)
#        for backend2 in backends:
#            t2 = backend2.to_backend(t1)
#            assert a == to_array(t2), f'conversion of random {shape(a)} from {backend1.name} to {backend2.name}'

def test_shaping():
    a1 = random_array(3,3)
    a2 = random_array(3,3)
    a_concat0 = [*a1, *a2]
    a_stack0 = [a1, a2]
    for backend in backends:
        t1 = backend.tensor(a1)
        t2 = backend.tensor(a2)

        t = backend.concat((t1, t2), axis=0)
        assert to_array(t) == a_concat0, f'{backend.name} concatenation of random {shape(a1)} with random {shape(a2)}'
        t = backend.stack((t1, t2), axis=0)
        assert to_array(t) == a_stack0, f'{backend.name} stacking of random {shape(a1)} with random {shape(a2)}'

def test_calculation():
    for backend in backends:
        t1 = backend.tensor([1.0,3.0,2.0,5.0,4.0])

        assert backend.argmax(t1) == 3, f'{backend.name} argmax'
        
        # matrix products
        t = backend.einsum('i,j->ij', t1, t1)
        assert to_array(t) == [ [ 1, 3, 2, 5, 4],
                                [ 3, 9, 6,15,12],
                                [ 2, 6, 4,10, 8],
                                [ 5,15,10,25,20],
                                [ 4,12, 8,20,16] ], f'{backend.name} double {shape(t1)} einsum'

        t = backend.softmax(t1, axis=0)
        assert to_array(t) == [ round(0.011656231246888638, ROUND_DIGITS),
                                round(0.08612854033708572, ROUND_DIGITS),
                                round(0.03168492019176483, ROUND_DIGITS),
                                round(0.6364086270332336, ROUND_DIGITS),
                                round(0.2341216504573822, ROUND_DIGITS) ], f'{backend.name} softmax'
                                
