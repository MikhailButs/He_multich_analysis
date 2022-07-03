import os
from PIL import Image, ImageFilter
import numpy as np
from numba import njit
from get_data import get_data
from matplotlib import pyplot as plt

dir2work = os.path.normpath(input('Input an abs link to images:    '))
try:
    images_list = os.listdir(dir2work)  # ['name1.jpg', 'name2.jpg', ...]
except FileNotFoundError:
    print('Invalid value')
    exit()

prev_image = []
current_image = []
differ_image = []

@njit
def check_limits(matrix):
    for i in matrix:
        for j in i:
            if j < 0.:
                j = 0.
            if j > 255.:
                j = 255.
    return matrix


int = []
int_ch = []
for img in images_list:
    ch1_data, ch2_data, ch3_data = get_data(os.path.join(dir2work, img))
    if images_list.index(img) > 0:
        current_images = np.array([ch1_data[0], ch2_data[0], ch3_data[0]])
        im = Image.fromarray(current_images[2]).filter(ImageFilter.MedianFilter(size=3)).convert('L')
        current_image = np.array(im)
        differ_image = current_image - prev_image
        # int.append(np.sum(differ_images[2]))
        # differ_images[2] = check_limits(differ_images[2])
        # int_ch.append(np.sum(differ_images[2]))
        # Image.fromarray(current_images[2]).show()
        im = Image.fromarray(differ_image)
        plt.imshow(im, cmap='turbo')
        plt.show()
        im.convert('RGB').save(os.path.join(os.path.join(os.getcwd(), f'diff_images'), img))
        print(images_list.index(img))
    elif images_list.index(img) == 0:
        current_image = np.array([ch1_data[0], ch2_data[0], ch3_data[0]])[2]
    prev_image = current_image

# print(int)
# print(int_ch)
# plt.plot(int, label='not ch')
# plt.plot(int_ch, label='ch')
# plt.legend()
# plt.show()
