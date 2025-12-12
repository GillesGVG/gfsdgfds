# demo_import_numpy.py
"""Demo file that imports numpy and runs a small array operation for testing in repo GillesGVG/gfsdgfds"""

try:
    import numpy as np
    print("numpy imported:", np.__version__)
    a = np.array([1, 2, 3])
    print("array + 1 ->", a + 1)
except Exception as e:
    print("Import failed:", e)

# End of file
