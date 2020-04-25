from flask import Flask
from flaskt import swagger

app = Flask(__name__)

app.register_blueprint(swagger.get_swagger())


@app.route('/vegetation-cover', methods=['GET'])
def vegetationCover():
    return 'WIP'

app.run()