# demo_import_pandas.py
"""Demo file that imports pandas and creates a small DataFrame for testing in repo GillesGVG/gfsdgfds"""

try:
    import pandas as pd
    print("pandas imported:", pd.__version__)
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    print("df:\n", df)
except Exception as e:
    print("Import failed:", e)

# End of file
