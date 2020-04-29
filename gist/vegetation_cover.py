import os
import numpy as np
import rasterio as ras
import rasterio.features as features
import rasterio.warp as warp
from gist import date_utils

image_path = os.path.join(os.path.dirname(__file__), 'resource/analytic.tif')
src = ras.open(image_path)

def get_file_name():
    return os.path.basename(src.name)

def get_cover():
    red = src.read(3).astype(float)
    nir = src.read(4).astype(float)
    np.seterr(divide='ignore', invalid='ignore')
    check = np.logical_or(red > 0, nir > 0)
    ndvi = np.where(check, (nir - red) / (nir + red), 0.0)
    return ndvi.mean()

def get_area():
    width = src.bounds.right - src.bounds.left
    height = src.bounds.top - src.bounds.bottom
    return width * height

def get_centroid():
    mask = src.dataset_mask()
    for geom, val in features.shapes(mask, transform=src.transform):
        geom = warp.transform_geom(
            src.crs, 'EPSG:4326', geom, precision=6)
        return geom

def get_image_time():
    image_time = src.tags(ns='TIFFTAG_DATETIME')
    if bool(image_time):
        return date_utils.convert_datetime_to_timestamp(image_time, '%Y:%m:%d %H:%M:%S')
    return ''