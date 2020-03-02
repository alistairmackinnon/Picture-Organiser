from PIL import Image, ExifTags
img = Image.open("/home/ali/Pictures/Loch Lomond/2012-05-29 15.52.18.jpg")
exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}

print(exif['DateTimeOriginal'])
