activate_this = '/home/flask/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from lookup_api import app

if __name__ == "__main__":
    app.run()