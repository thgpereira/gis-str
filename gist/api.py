from flask import Blueprint
from .vegetation_cover import VegetationCover

vc = VegetationCover()
bp = Blueprint('vegetation_cover', __name__, url_prefix='/vegetation-cover')

def get_blueprint():
    return bp

@bp.route('', methods=['GET'])
def get_data():
    return {
        'filename': vc.get_file_name(),
        'cover': vc.get_cover(),
        'area': vc.get_area(),
        'centroid': vc.get_centroid(),
        'local_time': vc.get_image_time()
    }