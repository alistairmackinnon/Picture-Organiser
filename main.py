from PIL import Image, ExifTags
import os

folder = "/home/ali/Pictures/nights out"


for root, directory, files in os.walk(folder):
    for file in files:
        try:
            file_path = os.path.join(folder, file)
            img = Image.open(file_path)
            exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
            print(file_path)
            print(exif['DateTimeOriginal'])
        except:
            continue
