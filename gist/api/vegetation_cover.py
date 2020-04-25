from flask import Blueprint

bp = Blueprint('vegetation_cover', __name__, url_prefix='/vegetation-cover')

def get_blueprint():
    return bp

@bp.route('', methods=['GET'])
def get_data():
    return {
        'filename': get_file_name(),
        'cover': get_cover(),
        'area': get_area(),
        'centroid': get_centroid(),
        'local_time': get_local_time()
    }

def get_file_name():
    return 'WIP'

def get_cover():
    return 'WIP'

def get_area():
    return 'WIP'

def get_centroid():
    return 'WIP'

def get_local_time():
    return 'WIP'