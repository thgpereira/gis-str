import os
import numpy as np
import rasterio as ras
import rasterio.features as features
import rasterio.warp as warp
from gist.date_utils import DateUtis

class VegetationCover:
    def __init__(self):
        image_path = os.path.join(os.path.dirname(__file__), 'resource/analytic.tif')
        self.src = ras.open(image_path)
        self.date_utils = DateUtis()

    def get_file_name(self):
        return os.path.basename(self.src.name)

    def get_cover(self):
        red = self.src.read(3).astype(float)
        nir = self.src.read(4).astype(float)
        np.seterr(divide='ignore', invalid='ignore')
        check = np.logical_or(red > 0, nir > 0)
        ndvi = np.where(check, (nir - red) / (nir + red), 0.0)
        return ndvi.mean()

    def get_area(self):
        width = self.src.bounds.right - self.src.bounds.left
        height = self.src.bounds.top - self.src.bounds.bottom
        return width * height

    def get_centroid(self):
        mask = self.src.dataset_mask()
        for geom, val in features.shapes(mask, transform=self.src.transform):
            geom = warp.transform_geom(
                self.src.crs, 'EPSG:4326', geom, precision=6)
            return geom

    def get_image_time(self):
        image_time = self.src.tags(ns='TIFFTAG_DATETIME')
        if bool(image_time):
            return date_utils.convert_datetime_to_timestamp(image_time, '%Y:%m:%d %H:%M:%S')
        return ''