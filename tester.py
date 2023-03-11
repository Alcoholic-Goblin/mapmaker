from PIL import Image

im = Image.open('2.png') # Can be many different formats.
pix = im.load()
print (im.size) # Get the width and hight of the image for iterating over
print (pix[7,8])  # Get the RGBA Value of the a pixel of an image
