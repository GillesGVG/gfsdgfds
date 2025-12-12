# demo_import_scipy.py
"""Demo file that imports scipy and runs a basic calculation"""

try:
    import numpy as np
    from scipy import stats
    print("scipy imported:", stats.__module__)
    x = np.array([1, 2, 3, 4, 5])
    print("mean:", np.mean(x), "median:", np.median(x))
    print("normal PDF at 0:", stats.norm.pdf(0))
except Exception as e:
    print("Import failed:", e)

# End of file
