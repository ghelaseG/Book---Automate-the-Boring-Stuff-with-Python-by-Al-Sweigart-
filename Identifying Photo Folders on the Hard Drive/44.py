#python3! - Write a program that goes through every folder on your hard drive and finds potential photo folders.

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/home'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg
        if not(filename.lower().endswith('jpg') or filename.lower().endswith('png')):
            numNonPhotoFiles += 1
            continue #skip to next filename

        #Open image file using Pillow
        try:
            im = Image.open(os.path.join(foldername, filename))
        except OSError:
            continue

        width, height = im.size

        #Check if width & height are larger than 500
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo
            numNonPhotoFiles += 1

    # If more than half of files were photos, print the absolute path of the folder
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername))
