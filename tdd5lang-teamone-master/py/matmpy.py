import pandas as pd

def mat_mpy(mat_a: pd.DataFrame, mat_b: pd.DataFrame) -> pd.DataFrame:
    """Return the mastrix-multiplication of mat_a and mat_b."""
    #figure out dimensions of the matrices, dimension validation    
    rows_a, cols_a = mat_a.shape
    rows_b, cols_b = mat_b.shape

    #user story 1:
    #As a user I want to multiply an NxM matrix with an MxP matrix and get back the NxP matrix product so I can do more general math.

    #user story 2:
    #As a user I want to get an "Incomptable Dimensions" error when I attempt to multiply matrices with incompatible dimensions so I know why the program failed.
    
    #NxM x MxP = NxP, M_a == M_b
    if cols_a != rows_b:
        raise ValueError("The matrices have incompatible dimensions")
    
    result_matrix = mat_a @ mat_b
    
    return result_matrix