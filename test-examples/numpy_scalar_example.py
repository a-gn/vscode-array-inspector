"""
Example script to test the Array Inspector extension with NumPy scalars.

NumPy scalars are 0-dimensional arrays that result from operations like mean(), sum(), etc.
They should display "(scalar)" as their shape in the Array Inspector.

To test:
1. Install numpy: pip install numpy
2. Set a breakpoint at line 17
3. Start debugging (F5)
4. Click on scalar variable names to see them in the Array Inspector
5. Verify that their shape shows as "(scalar)"
"""

import numpy as np


def main():
    # Create a NumPy array
    arr = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  # Breakpoint here

    # Create various NumPy scalars from operations
    mean_value = np.mean(arr)  # numpy.float64 scalar
    sum_value = np.sum(arr)  # numpy.float64 scalar
    max_value = np.max(arr)  # numpy.float64 scalar
    min_value = np.min(arr)  # numpy.float64 scalar

    # Create scalars from indexing
    first_element = arr[0, 0]  # numpy.float64 scalar

    # Create scalars from numpy functions
    scalar_int = np.int32(42)  # numpy.int32 scalar
    scalar_float = np.float32(3.14)  # numpy.float32 scalar
    scalar_bool = np.bool_(True)  # numpy.bool_ scalar

    # Create scalars from array operations
    dot_product = np.dot(arr[0], arr[1])  # numpy.float64 scalar

    # Print some info (for verification outside the debugger)
    print(f"Mean: {mean_value}, type: {type(mean_value)}, shape: {mean_value.shape}")
    print(f"Sum: {sum_value}, type: {type(sum_value)}, shape: {sum_value.shape}")
    print(f"Scalar int: {scalar_int}, type: {type(scalar_int)}, shape: {scalar_int.shape}")
    print(
        f"Scalar float: {scalar_float}, type: {type(scalar_float)}, shape: {scalar_float.shape}"
    )
    print(
        f"Scalar bool: {scalar_bool}, type: {type(scalar_bool)}, shape: {scalar_bool.shape}"
    )

    # Verify they are indeed numpy scalars with empty tuple shape
    assert mean_value.shape == ()
    assert sum_value.shape == ()
    assert scalar_int.shape == ()

    print("\nAll scalars have shape () as expected!")


if __name__ == "__main__":
    main()
