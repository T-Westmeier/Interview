from interview.test_file import add_vars
import numpy as np

def test_add_vars_integers():
    assert add_vars(1, 2) == 3

def test_add_vars_floats():
    assert add_vars(1.5, 2.5) == 4.0

def test_add_vars_arrays():
    assert np.array_equal(add_vars(np.array([1, 2]), np.array([3, 4])), np.array([4, 6]))

def test_add_vars_strings():
    assert add_vars("Hello, ", "world!") == "Hello, world!"