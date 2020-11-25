#!/usr/bin/python
from PIL import Image
import numpy as np

SCREEN_WIDTH=1920
SCREEN_HEIGHT=1080

h = 'eee3e7'
rbg = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

array = np.zeros([SCREEN_HEIGHT, SCREEN_WIDTH, 3], dtype=np.uint8)
array[:,:] = rbg

img = Image.fromarray(array)
img.save('wallcolor_{}_{}_{}.png'.format(rbg[0], rbg[1], rbg[2]))