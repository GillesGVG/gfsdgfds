# demo_import.py
"""Demo file that imports a package for testing in repo GillesGVG/gfsdgfds"""

try:
    import requests
    print("requests imported:", requests.__version__)
except Exception as e:
    print("Import failed:", e)

# End of file
