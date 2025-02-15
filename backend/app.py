from flask import Flask
from routes import api_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
