#!/usr/bin/python
from PIL import Image
import numpy as np

SCREEN_WIDTH=1080
SCREEN_HEIGHT=2280

h = input("Enter hex code: ").strip('#')
rgb2 = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

h = input("Enter hex code: ").strip('#')
rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

array = np.zeros([SCREEN_HEIGHT, SCREEN_WIDTH, 3], dtype=np.uint8)
array[:,:] = rgb

array[:int(SCREEN_HEIGHT/((1+np.sqrt(5))/2)), :] = rgb2

img = Image.fromarray(array)
img.save('wallcolor_{}_{}_{}.png'.format(rgb[0], rgb[1], rgb[2]))