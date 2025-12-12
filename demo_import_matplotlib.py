# demo_import_matplotlib.py
"""Demo file that imports matplotlib, creates a simple plot, and saves it to demo_plot.png"""

try:
    import matplotlib
    import matplotlib.pyplot as plt
    print("matplotlib imported:", matplotlib.__version__)
    plt.plot([0, 1, 2, 3], [0, 1, 4, 9])
    plt.title("Demo plot")
    plt.savefig("demo_plot.png")
    print("Saved demo_plot.png")
except Exception as e:
    print("Import failed:", e)

# End of file
