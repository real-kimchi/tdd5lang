import sys

import pandas as pd
from matmpy import mat_mpy

assert len(sys.argv) == 3, "Expecting arguments mat1.csv mat2.csv"

#cmd arguments
_, f_mat1, f_mat2 = sys.argv

#reading matrices from csv
mat_a = pd.read_csv(f_mat1, index_col=None, header=None)
mat_b = pd.read_csv(f_mat2, index_col=None, header=None)

#matrix multiply func
ans = mat_mpy(mat_a, mat_b)

#output multiplied matrix
ans.to_csv(sys.stdout)

except AssertionError as e:
    sys.stderr.write(str(e) + "\n")

except ValueError as e:
    sys.stderr.write(str(e) + "\n")

except Exception as e:
    sys.stderr.write("An unexpected error occurred: " + str(e) + "\n")