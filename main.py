import os
from os.path import join

from lib import img_files
from lib import img_names


def main():
    extraction_path = f"data/originals"
    success_path = f"data/success"
    failure_path = f"data/failure"

    print(f"extract from: {extraction_path}")
    print(f"success     : {extraction_path}")
    print(f"failure     : {failure_path}")
    print()

    if os.path.exists(success_path) or os.path.exists(failure_path):
        raise FileExistsError("please delete/rename the success and failure directories to avoid name collisions")
    os.mkdir(success_path)
    os.mkdir(failure_path)

    print("extract/convert...")
    for image in os.listdir(extraction_path):
        if img_names.is_covered(image):
            img_files.convert_png_to_jpg(image, extraction_path, success_path)
        else:
            img_files.move(image, extraction_path, failure_path)

    print("add time...")
    for image in os.listdir(success_path):
        time = img_names.extract(image)

        path = join(success_path, image)
        img_files.change_date(path, time)


if __name__ == '__main__':
    main()
