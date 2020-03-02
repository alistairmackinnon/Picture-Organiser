from PIL import Image, ExifTags
import os
from datetime import datetime
from shutil import copyfile

src_folder = "/home/ali/Pictures/nights out"
dst_folder = "/home/ali/Pictures"


for root, directory, files in os.walk(src_folder):
    for file in files:
        try:
            src_file_path = os.path.join(src_folder, file)
            img = Image.open(src_file_path)
            exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
            crt_timestamp = exif['DateTimeOriginal']
            print(src_file_path)
            date_str = crt_timestamp[:10].replace(':', '-')
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            print(date_obj.year)

        except:
            continue
