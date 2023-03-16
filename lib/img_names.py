import re
from datetime import datetime


def is_covered(filename) -> bool:
    if re.match(r"Screenshot_20[0-2][0-9][0-1][0-9][0-3][0-9]-[0-9]+.*?", filename):
        return True
    if re.match(r"IMG-20[0-2][0-9][0-1][0-9][0-3][0-9]-WA[0-9]+.*?", filename):
        return True
    if re.match(r"IMG_20[0-2][0-9][0-1][0-9][0-3][0-9]_[0-9]+.*?", filename):
        return True
    return False


def extract(filename) -> str:
    if re.match(r"Screenshot_20[0-2][0-9][0-1][0-9][0-3][0-9]-[0-9]+.*?", filename):
        return _extract_screenshot(filename)
    if re.match(r"IMG-20[0-2][0-9][0-1][0-9][0-3][0-9]-WA[0-9]+.*?", filename):
        return _extract_whatsapp(filename)
    if re.match(r"IMG_20[0-2][0-9][0-1][0-9][0-3][0-9]_[0-9]+.*?", filename):
        return _extract_img(filename)


def _extract_screenshot(filename) -> str:
    """
    extract datetime

    :param filename: like "Screenshot_20170201-172235.png"
    :return: datetime
    """
    year = int(filename[11:15])
    month = int(filename[15:17])
    day = int(filename[17:19])
    hour = int(filename[20:22])
    minute = int(filename[22:24])
    second = int(filename[24:26])

    return datetime(year, month, day, hour, minute, second).strftime("%Y:%m:%d %H:%M:%S")


def _extract_img(filename) -> str:
    """
        extract datetime

        :param filename: like "IMG_20190811_202425.jpg"
        :return: datetime
        """
    year = int(filename[4:8])
    month = int(filename[8:10])
    day = int(filename[10:12])
    hour = int(filename[13:15])
    minute = int(filename[15:17])
    second = int(filename[17:19])

    return datetime(year, month, day, hour, minute, second).strftime("%Y:%m:%d %H:%M:%S")


def _extract_whatsapp(filename) -> str:
    """
    extract datetime

    :param filename: like "IMG-20150721-WA0000.png"
    :return: datetime
    """
    year = int(filename[4:8])
    month = int(filename[8:10])
    day = int(filename[10:12])
    hour = 12
    minute = 0
    second = 0

    return datetime(year, month, day, hour, minute, second).strftime("%Y:%m:%d %H:%M:%S")
