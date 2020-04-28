import os
import numpy
import rasterio
import rasterio.features
import rasterio.warp
from flask import Blueprint

bp = Blueprint('vegetation_cover', __name__, url_prefix='/vegetation-cover')
image_path = os.path.join(os.path.dirname(__file__), 'resource/analytic.tif')
src = rasterio.open(image_path)

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
    return os.path.basename(src.name)

def get_cover():
    red = src.read(3).astype(float)
    nir = src.read(4).astype(float)
    numpy.seterr(divide='ignore', invalid='ignore')
    check = numpy.logical_or(red > 0, nir > 0)
    ndvi = numpy.where(check, (nir - red) / (nir + red), 0.0)
    return ndvi.mean()

def get_area():
    width = src.bounds.right - src.bounds.left
    height = src.bounds.top - src.bounds.bottom
    return width * height

def get_centroid():
    mask = src.dataset_mask()
    for geom, val in rasterio.features.shapes(mask, transform=src.transform):
        geom = rasterio.warp.transform_geom(
            src.crs, 'EPSG:4326', geom, precision=6)
        return geom

def get_local_time():
    return 'WIP'