from flask import Flask
from gist import swagger
from gist import vegetation_cover

app = Flask(__name__)

app.register_blueprint(swagger.get_swagger())
app.register_blueprint(vegetation_cover.get_blueprint())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)