#!python3 : Extend resizeAndAddLogo.py to process GIF and BMP images as well.
# Change the code so that the file extension check is case insensitive.
# Modify resizeAndAddLogo.py so that the image must be at least twice the width and height of the logo image before the logo is pasted.


import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
#Loop over all files in the working directory
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
            or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')) \
            or filename == LOGO_FILENAME:
        continue #skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

    # Resize the image.
    print('Resizing {}...'.format(filename))
    im = im.resize((width, height))

    # Add logo.
    width, height = im.size
    if width < logo.width * 2 or height < logo_height * 2:
        print("Logo wouldn't look good, skipped")
    else:
        print('Adding logo to {}...'.format(filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))
