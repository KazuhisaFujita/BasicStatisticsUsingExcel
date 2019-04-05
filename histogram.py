#---------------------------------------
#Since : 2019/03/07
#Update: 2019/04/02
# -*- coding: utf-8 -*-
#---------------------------------------
import numpy as np
import six
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.random.normal(65,10, 100).astype(np.int)

#x[99] = 500

for i in range(10):
    for j in range(10):
        six.print_(str(x[i + j * 10]), "&", end=" ")

    print("")

hist, classes = np.histogram(x, range(0, 120, 10))

for i in range(np.size(hist)):
    print(classes[i], classes[i+1] - 1, "&",  hist[i])

print(np.average(x))
print(np.median(x))
print(np.var(x))
print(np.std(x))

np.savetxt("hist.txt", x, fmt=['%d'])

# plt.hist(x, range=(0,100))
# plt.savefig("hist.eps")
