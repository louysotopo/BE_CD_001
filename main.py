#Libraries
from flask_cors import CORS
from app import app
from app.routes import api
#Configuration 
CORS(app,resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'





