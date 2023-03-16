import unittest

from lib import img_names


class Testing(unittest.TestCase):
    images = {
        "Screenshot_20170201-172235.png": "2017:02:01 17:22:35",
        "Screenshot_20170201-172235": "2017:02:01 17:22:35",
        "IMG-20150721-WA0000.png": "2015:07:21 12:00:00",
        "IMG-20150721-WA0000": "2015:07:21 12:00:00",
        "IMG_20190811_202425.jpg": "2019:08:11 20:24:25",
        "IMG_20190811_202425": "2019:08:11 20:24:25",
        "Screenshot_20190720-013426": "2019:07:20 01:34:26"
    }

    def test_check(self):
        self.assertFalse(img_names.is_covered("unknown.png"))

        for filename in self.images:
            self.assertTrue(img_names.is_covered(filename))

    def test_extract(self):
        for filename, date_time in self.images.items():
            output = img_names.extract(filename)
            self.assertEqual(output, date_time)

    def test_extract_screenshot(self):
        for filename in ["Screenshot_20170201-172235.png", "Screenshot_20170201-172235"]:
            output = img_names._extract_screenshot(filename)
            self.assertEqual(output, self.images[filename])

    def test_extract_whatsapp(self):
        for filename in ["IMG-20150721-WA0000.png", "IMG-20150721-WA0000"]:
            output = img_names._extract_whatsapp(filename)
            self.assertEqual(output, self.images[filename])

    def test_extract_img(self):
        for filename in ["IMG_20190811_202425.jpg", "IMG_20190811_202425"]:
            output = img_names._extract_img(filename)
            self.assertEqual(output, self.images[filename])


if __name__ == '__main__':
    unittest.main()
