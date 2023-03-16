import shutil
from os.path import join

import piexif
from PIL import Image


def move(file_name, source, destination):
    shutil.move(f"{source}/{file_name}", f"{destination}/{file_name}")


def change_date(file_name, datetime):
    exif_dict = piexif.load(file_name)
    exif_dict['0th'][piexif.ImageIFD.DateTime] = datetime
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = datetime
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = datetime
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, file_name)


def convert_png_to_jpg(filename, orig_dir, new_dir):
    img = Image.open(join(orig_dir, filename))
    img.save(join(new_dir, f"{filename[:-3]}jpg"))
