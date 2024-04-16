


import matplotlib.pyplot as plt

data = open('UAV_data.txt', 'r')

time = []
concentration = []
x_coord = []
y_coord = []

lines = data.readlines()
print(lines)

for line in lines[1:]:
    list = line.split('\t')
    time += [int(list[0])]
    concentration += [float(list[1])]
    x_coord += [float(list[2])]
    y = list[3]
    y = y.strip()
    y_coord += [float(y)]

print(time)
print(concentration)
print(x_coord)
print(y_coord)


plt.subplot(121)
plt.plot(x_coord, y_coord)
plt.title('Flight path of UAV')
plt.xlabel('x_coord')
plt.ylabel('y_coord')
plt.subplot(122)
plt.plot(time, concentration, 'r')
plt.title('NO2 conc over time')
plt.xlabel('t')
plt.ylabel('NO2_conc')



plt.show()
data.close()
