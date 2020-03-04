from PIL import Image, ExifTags
import PIL
import os
from datetime import datetime
from shutil import copyfile

# declare variables for use throughout
src_folder = "/home/ali/Pictures/"
dst_parent = "/home/ali/Pictures/Yearly_Archive"
error_count = 0
error_list = []


# define functions
def get_year(file_in):
    exif = {ExifTags.TAGS[k]: v for k, v in file_in._getexif().items() if k in ExifTags.TAGS}
    try:
        # where possible, extract the year from the metadata
        crt_timestamp = exif['DateTimeOriginal']
        date_str = crt_timestamp[:10].replace(':', '-')
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        year_str = date_obj.year
        return year_str
    except KeyError:
        # where there is no year available, default folder
        return 'No_Year'


# create the parent directory if it does not exist
if not os.path.exists(dst_parent):
    os.mkdir(dst_parent)

for root, directory, files in os.walk(src_folder):
    if dst_parent not in root:
        for file in files:
            try:
                src_file_path = os.path.join(root, file)
                img = Image.open(src_file_path)
                year = get_year(img)
                dst_dir = os.path.join(dst_parent, str(year))
                # if the directory exists
                full_file = os.path.join(dst_dir, file)
                if os.path.isdir(dst_dir):
                    # if the file does not exist
                    if not os.path.exists(full_file):
                        copyfile(src_file_path, full_file)
                        print(f'{full_file} - Copied')
                # if the directory doesn't exist, create it then copy
                else:
                    os.mkdir(dst_dir)
                    copyfile(src_file_path, full_file)
            # log all fails in a list
            except (PIL.UnidentifiedImageError, AttributeError):
                error_count += 1
                error_list.append(src_file_path)
                pass

# write fails to file
log = open('/home/ali/Pictures/log.txt', 'a')
for error in error_list:
    log.write(error + '\n')
