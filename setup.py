from flask import Flask
from gist.api import swagger
from gist.api import vegetation_cover

app = Flask(__name__)

app.register_blueprint(swagger.get_swagger())
app.register_blueprint(vegetation_cover.get_blueprint())

app.run()