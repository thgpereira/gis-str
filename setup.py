from flask import Flask
from gist.swagger import Swagger
from gist import api

app = Flask(__name__)
swagger = Swagger()

app.register_blueprint(swagger.get_swagger())
app.register_blueprint(api.get_blueprint())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)