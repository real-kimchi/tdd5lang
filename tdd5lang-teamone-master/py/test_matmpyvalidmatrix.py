import pandas as pd
from pandas.testing import assert_frame_equal
from matmpy import mat_mpy

def test_valid_matrix():
    """Test multiplication of incompatible matrices"""
    #As a user I want to get an "Incomptable Dimensions" error when I attempt to multiply matrices with incompatible dimensions so I know why the program failed.
    
    mat_a = pd.DataFrame([
        [1, 2, 3],
        [4, 5, 6]
    ])
    
    mat_b = pd.DataFrame([
        [1, 2],
        [3, 4]
    ])
    
    try:
        result = mat_mpy(mat_a, mat_b)
    except ValueError as e:
        assert "The matrices have incompatible dimensions" in str(e), f"Expected an error with 'The matrices have incompatible dimensions', but got {e}"
        return  # Test passed, return successfully
    assert False, "Expected a ValueError for incompatible matrices, but multiplication was successful."
