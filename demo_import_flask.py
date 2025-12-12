# demo_import_flask.py
"""Demo file that imports Flask and creates a minimal app object for testing"""

try:
    from flask import Flask
    print("flask imported")
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello from demo_import_flask'

    if __name__ == "__main__":
        app.run(port=5001)
except Exception as e:
    print("Import failed:", e)

# End of file
