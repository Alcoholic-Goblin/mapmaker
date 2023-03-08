import random
import time
from PIL import Image
import numpy as np
import csv
import copy
from datetime import datetime
import glob
import contextlib
import os


fp_in = "working/*.png"
fp_out = "final.gif"

# use exit stack to automatically close opened images
with contextlib.ExitStack() as stack:

    # lazily load images
    imgs = (stack.enter_context(Image.open(f))
            for f in sorted(glob.glob(fp_in)))

    # extract  first image from iterator
    img = next(imgs)

    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=100, loop=0)  
