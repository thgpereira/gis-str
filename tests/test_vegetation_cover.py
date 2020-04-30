import unittest2
import numpy.testing
from gist.vegetation_cover import VegetationCover

class TestVegetationCover(unittest2.TestCase):
    def setUp(self):
        self.vc = VegetationCover()

    def test_file_name(self):
        file_name = self.vc.get_file_name()
        self.assertEqual(file_name, 'analytic.tif', 'Should be analytic.tif')

    def test_get_cover(self):
        cover = self.vc.get_cover()
        self.assertEqual(cover, 0.49715062845406466, 'Should be 0.49715062845406466')

    def test_get_area(self):
        area = self.vc.get_area()
        self.assertEqual(area, 1267031.25, 'Should be 1267031.25')

    def test_get_centroid(self):
        centroid = self.vc.get_centroid()
        self.assertTrue(centroid)

        cord_array = [[
            [-47.604134, -15.854655], 
            [-47.604232, -15.862331], 
            [-47.590324, -15.862498], 
            [-47.590226, -15.854821], 
            [-47.604134, -15.854655]
        ]]
        numpy.testing.assert_array_equal(centroid['coordinates'], cord_array)        

    def test_local_time(self):
        local_time = self.vc.get_image_time()
        self.assertEqual(local_time, '', 'Should be empty')


if __name__ == "__main__":
    unittest.main()