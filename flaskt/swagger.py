from flask_swagger_ui import get_swaggerui_blueprint

def get_swagger():
    return get_swaggerui_blueprint(
        '',
        '../static/swagger_api.yml',
        config={
            'app_name': "Strider - Desafio"
        }
    )