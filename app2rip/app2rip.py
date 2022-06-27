import ripper as rp
import matplotlib.pyplot as plt
from os import path

sht_dir, sht_num = path.split(input('Abs link to .sht file:    '))
sht_num = int(sht_num[3:-4])
data, link = rp.extract(sht_dir, sht_num,
                        ['D-alfa верхний купол', 'Газонапуск He капиляр', 'N II'])

x, y = rp.x_y(data[59])
plt.subplot(3, 1, 1)
plt.plot(x, y)
plt.title('D-alpha верхний купол')

x, y = rp.x_y(data[35])
plt.subplot(3, 1, 2)
plt.plot(x, y)
plt.title('N II')

x, y = rp.x_y(data[81])
plt.subplot(3, 1, 3)
plt.plot(x, y)
plt.title('Газонапуск He капилляр')

plt.plot(y)
plt.tight_layout()
plt.show()
