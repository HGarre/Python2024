import numpy as np
import matplotlib.pyplot as plt

data = np.array([9,18,13,9,6,6,16,6,17,10,15,16,13,11,13,8,20,6,18,11])
print(data)
print(min(data))
print(max(data))

plt.hist(data, bins = max(data)-min(data)+1, range = (min(data),max(data)+1), align = 'left')
plt.yticks([1,2,3,4])
plt.xticks(range(min(data), max(data)+1))
plt.title('Simple Histogram')
plt.ylabel('Frequency')

plt.show()