from PIL import Image, ExifTags
import PIL
import os
from datetime import datetime
from shutil import copyfile


def get_year(file_in):
    exif = {ExifTags.TAGS[k]: v for k, v in file_in._getexif().items() if k in ExifTags.TAGS}
    crt_timestamp = exif['DateTimeOriginal']
    print(src_file_path)
    date_str = crt_timestamp[:10].replace(':', '-')
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    year_str = date_obj.year
    return year_str


src_folder = "/home/ali/Pictures/Loch Lomond"
dst_parent = "/home/ali/Pictures/Yearly_Archive"
error_count = 0
error_list = []

if not os.path.exists(dst_parent):
    os.mkdir(dst_parent)

for root, directory, files in os.walk(src_folder):
    for file in files:
        try:
            src_file_path = os.path.join(src_folder, file)
            img = Image.open(src_file_path)
            year = get_year(img)
            dst_dir = os.path.join(dst_parent, str(year))
            if os.path.isdir(dst_dir):
                copyfile(src_file_path, os.path.join(dst_dir, file))
            else:
                os.mkdir(dst_dir)

        except PIL.UnidentifiedImageError:
            error_count += 1
            error_list.append(src_file_path)
            pass

print(error_list)
