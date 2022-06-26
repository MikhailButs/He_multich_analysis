import ripper as rp
import matplotlib.pyplot as plt

data, link = rp.extract(r'C:\Users\joana\PycharmProjects\He_multich_analysis\app2rip', 40264,
                        ['D-alpha', 'D-alfa', 'He', 'N II'])

x, y = rp.x_y(data[59])

plt.plot(y)
plt.show()
