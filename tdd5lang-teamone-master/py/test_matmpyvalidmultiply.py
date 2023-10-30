import pandas as pd
from pandas.testing import assert_frame_equal
from matmpy import mat_mpy

def test_valid_multiply():
        """Test multiply of compatible matrices"""
        #As a user I want to multiply an NxM matrix with an MxP matrix and get back the NxP matrix product so I can do more general math.
        
        mat_a = pd.DataFrame([
            [1, 2],
            [3, 4]
        ])
    
        mat_b = pd.DataFrame([
            [2, 0],
            [1, 2]
        ])
    
        expected_result = pd.DataFrame([
            [4, 4],
            [10, 8]
        ])
    
        result = mat_mpy(mat_a, mat_b)
        assert result.equals(expected_result), f"Expected {expected_result}, got {result}"