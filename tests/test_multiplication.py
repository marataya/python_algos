import pytest

# Test
# two positive numbers
# two negative numbers
# identity mult
# multiplicaiton by 0
# floats

# test cases
product = [
    (2, 3, 6),
    (9, 0, 0),
    (-2, -3, -6),
    (-2, 3, -6),
    (2.5, 6.7, 16.75),
]
@pytest.mark.parametrize('a, b, product', product)
def test_multiplication(a, b, product):
    assert a * b == product
