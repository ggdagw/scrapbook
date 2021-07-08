import numpy as np


def clip(a, min_value, max_value):
    return min(max(a, min_value), max_value)

# note the instance of a class is passed in
def compute(array_1, array_2, myparams, a, b, c):
    """
    This function must implement the formula
    np.clip(array_1, 2, 10) * a + array_2 * b + c

    array_1 and array_2 are 2D.
    """
    x_max = array_1.shape[0]
    y_max = array_1.shape[1]

    assert array_1.shape == array_2.shape

    result = np.zeros((x_max, y_max), dtype=array_1.dtype)

    for x in range(x_max):
        for y in range(y_max):
            tmp = clip(array_1[x, y], 2, 10)
            tmp = tmp * a + array_2[x, y] * b
            result[x, y] = tmp + c

    # here we access a data member of the object passed in
    print myparams.d

    return result
