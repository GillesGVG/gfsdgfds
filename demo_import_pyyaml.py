# demo_import_pyyaml.py
"""Demo file that imports PyYAML and loads a simple YAML string"""

try:
    import yaml
    print("PyYAML imported:", getattr(yaml, '__version__', 'unknown'))
    data = yaml.safe_load("""\
a: 1
b:
  - 2
  - 3
""")
    print("Loaded YAML:", data)
except Exception as e:
    print("Import failed:", e)

# End of file
