import os
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from get_data import get_data

dir2work = os.path.normpath(input('Input an abs link:   '))
images_list = os.listdir(dir2work)  # ['name1.jpg', 'name2.jpg', ...]
intensity_list = ['' for i in range(len(images_list))]  # [[ch1, ch2, ch3], [ch1, ch2, ch3], ...]
ch1_int = []
ch2_int = []
ch3_int = []

for img in images_list:
    ch1_data, ch2_data, ch3_data = get_data(os.path.join(dir2work, img))
    temp_intensity = [ch1_data[1], ch2_data[1], ch3_data[1]]
    intensity_list[images_list.index(img)] = temp_intensity
    print(f'Image {images_list.index(img)+1} made')

for i in range(len(intensity_list)):
    ch1_int.append(intensity_list[i][0])
    ch2_int.append(intensity_list[i][1])
    ch3_int.append(intensity_list[i][2])

print(f'Ch1 intensity {ch1_int}')
print(f'Ch2 intensity {ch2_int}')
print(f'Ch3 intensity {ch3_int}')

plt.subplot(3, 1, 1)
plt.title('channel 1')
plt.plot(ch1_int)

plt.subplot(3, 1, 2)
plt.title('channel 2')
plt.plot(ch2_int)

plt.subplot(3, 1, 3)
plt.title('channel 3')
plt.plot(ch3_int)

plt.tight_layout()
plt.show()
