from flask import Flask

app = Flask(__name__)

from main import app

app.run(debug=False,host='0.0.0.0')