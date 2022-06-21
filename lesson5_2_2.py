import numpy as np
import matplotlib.pyplot as plt

x = []
for i in range(10):
    n = np.random.randint(0, 10, 10)
    x.append(sum(n))
    print(n)
    i += 1
num_bins = 5
n, bins, patches = plt.hist(x, num_bins)
plt.xlabel('Sum')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()
