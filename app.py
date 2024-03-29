import os
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from get_data import get_data3
import numpy as np
import app2rip.ripper as rp

dir2work = os.path.normpath(input('Input an abs link to images:    '))
try:
    images_list = os.listdir(dir2work)  # ['name1.jpg', 'name2.jpg', ...]
except FileNotFoundError:
    print('Invalid value')
    exit()

ax_type = input('Frames or Time(ms) X-axis? (F/T):    ')
time_step = 0

if ax_type == 'F' or ax_type == 'f':
    ax_type = 'f'
    print('Frames selected')
elif ax_type == 'T' or ax_type == 't':
    print('Time selected')
    ax_type = 't'

    time_step = input('Set time interval (ms):    ')
    try:
        time_step = float(time_step)
    except ValueError:
        print('Invalid value')
        exit()

    exposure = input('Set exposure (ms):    ')
    try:
        exposure = float(exposure)
    except ValueError:
        print('Invalid value')
        exit()

    initial_time = input('Set trigger time (ms):    ')
    try:
        initial_time = float(initial_time)
    except ValueError:
        print('Invalid value')
        exit()
else:
    print('Invalid value')
    exit()

if ax_type == 't':
    sht_path = os.path.abspath(input('Abs link to .sht file:    '))
    sht_dir, sht_num = os.path.splitext(sht_path)
    try:
        # sht_num = int(sht_num[3:-4])
        data, link = rp.extract(sht_path, None)
    except ValueError:
        print('Invalid value')
        exit()

    for i in data:
        print(i, '   ', data[i]['name'])

    plots = input('Input plot indexes (separator - space):    ')
    plots = plots.split(' ')
    for i in range(len(plots)):
        plots[i] = int(plots[i])

    # D_alpha_high_x, D_alpha_high_y = rp.x_y(data[59])
    # D_alpha_high_y = np.array(D_alpha_high_y)
    # D_alpha_high_y = D_alpha_high_y / np.sum(D_alpha_high_y) * len(D_alpha_high_y)
    # D_alpha_high_x = np.array(D_alpha_high_x) * 1000 - 100
    # plt.plot(D_alpha_high_x, D_alpha_high_y)
    for i in plots:
        x, y = rp.x_y(data[i])
        y = np.array(y)
        y = y / np.sum(y) * len(y)
        x = np.array(x) * 1000 - 100
        plt.plot(x, y, label=data[i]['name'])



intensity_list = ['' for i in range(len(images_list))]  # [[ch1, ch2, ch3], [ch1, ch2, ch3], ...]
ch1_int = []
ch2_int = []
ch3_int = []

time_list = [step * time_step + initial_time + exposure/2 for step in range(len(images_list))] if ax_type == 't' else []


for img in images_list:
    ch1_data, ch2_data, ch3_data = get_data3(os.path.join(dir2work, img))
    temp_intensity = [ch1_data[1], ch2_data[1], ch3_data[1]]
    intensity_list[images_list.index(img)] = temp_intensity
    print(f'Image {images_list.index(img)+1} from {len(images_list)} made')

for i in range(len(intensity_list)):
    ch1_int.append(intensity_list[i][0])
    ch2_int.append(intensity_list[i][1])
    ch3_int.append(intensity_list[i][2])

ch1_int = np.array(ch1_int)
ch1_int = ch1_int / np.sum(ch1_int) * len(ch1_int)
# print(f'Ch1 intensity {ch1_int}')
ch2_int = np.array(ch2_int)
ch2_int = ch2_int / np.sum(ch2_int) * len(ch2_int)
# print(f'Ch2 intensity {ch2_int}')
ch3_int = np.array(ch3_int)
ch3_int = ch3_int / np.sum(ch3_int) * len(ch3_int)
# print(f'Ch3 intensity {ch3_int}')

# x = [''for i in arange(78.145, 87.520, 0.625)] #40264_data

# plt.subplot(3, 1, 1)
# plt.title('I(t) channel 1 (728)' if ax_type == 't' else 'I(N) channel 1 (728)')
plt.plot(time_list, ch1_int, 'r.-', label='CH1') if ax_type == 't' else plt.plot(ch1_int, 'r.-', label='CH1')

# plt.subplot(3, 1, 2)
# plt.title('I(t) channel 2 (706)' if ax_type == 't' else 'I(N) channel 2 (706)')
plt.plot(time_list, ch2_int, 'r.-', label='CH2') if ax_type == 't' else plt.plot(ch2_int, 'r.-', label='CH2')

# plt.subplot(3, 1, 3)
# plt.title('I(t) channel 3 (667)' if ax_type == 't' else 'I(N) channel 3 (667)')
plt.plot(time_list, ch3_int, 'r.-', label='CH3') if ax_type == 't' else plt.plot(ch3_int, 'r.-', label='CH3')
# plt.legend()

plt.legend()
plt.tight_layout()
plt.show()
