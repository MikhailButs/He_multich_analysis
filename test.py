from cine_reader import Cine
from matplotlib import pyplot as plt
import numpy as np
from silx.math import medfilt2d

cine = Cine(r"D:\home\projects\ELM\data\cine\discharge40411_1000_struya_Nmoda.cine")
frame = np.array(cine.get_frame(1))
print('Mean', np.mean(frame))
print('Sigma', np.std(frame))
one = frame[0:331, 210:531]
two = frame[476:757, 232:510]
three = frame[27:347, 660:954]
four = frame[458:768, 658:970]
frame_f = list(frame.flatten())
for i in (one, two, three, four):
    print(np.mean(i), np.std(i))
    for j in i.flatten():
        frame_f.remove(j)
frame_f = np.array(frame_f)
print(np.mean(frame_f), np.std(frame_f))
# plt.hist(medfilt2d(frame, kernel_size=3).flatten(), bins=10)
cine.close()
