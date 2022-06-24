import os
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from get_data import get_data

dir2work = os.path.normpath(input('Input an abs link:    '))
ax_type = input('Frames or Time(ms) X-axis? (F/T):    ')
time_step = 0

if ax_type == 'F' or 'f':
    ax_type = 'f'
    print('Frames selected')
elif ax_type == 'T' or 't':
    print('Time selected')
    ax_type = 't'
    time_step = input('Set time interval (ms):    ')
    try:
        time_step = float(time_step)
    except ValueError:
        print('Invalid value')
        exit()
else:
    print('Invalid value')
    exit()

images_list = os.listdir(dir2work)  # ['name1.jpg', 'name2.jpg', ...]
intensity_list = ['' for i in range(len(images_list))]  # [[ch1, ch2, ch3], [ch1, ch2, ch3], ...]
ch1_int = []
ch2_int = []
ch3_int = []
time_list = [step * time_step for step in range(len(images_list))] if ax_type == 't' else []

for img in images_list:
    ch1_data, ch2_data, ch3_data = get_data(os.path.join(dir2work, img))
    temp_intensity = [ch1_data[1], ch2_data[1], ch3_data[1]]
    intensity_list[images_list.index(img)] = temp_intensity
    print(f'Image {images_list.index(img)+1} from {len(images_list)} made')

for i in range(len(intensity_list)):
    ch1_int.append(intensity_list[i][0])
    ch2_int.append(intensity_list[i][1])
    ch3_int.append(intensity_list[i][2])

print(f'Ch1 intensity {ch1_int}')
print(f'Ch2 intensity {ch2_int}')
print(f'Ch3 intensity {ch3_int}')

plt.subplot(3, 1, 1)
plt.title('I(t) channel 1 (728)' if ax_type == 't' else 'I(N) channel 1 (728)')
plt.plot(ch1_int, 'r.-') if ax_type == 't' else plt.plot(time_list, ch1_int, 'r.-')

plt.subplot(3, 1, 2)
plt.title('I(t) channel 2 (706)' if ax_type == 't' else 'I(N) channel 2 (706)')
plt.plot(ch2_int, 'r.-') if ax_type == 't' else plt.plot(time_list, ch2_int, 'r.-')

plt.subplot(3, 1, 3)
plt.title('I(t) channel 3 (667)' if ax_type == 't' else 'I(N) channel 3 (667)')
plt.plot(ch3_int, 'r.-') if ax_type == 't' else plt.plot(time_list, ch3_int, 'r.-')

plt.tight_layout()
plt.show()
