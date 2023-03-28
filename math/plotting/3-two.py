#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# your code here
fig, ax = plt.subplots()
ax.plot(x, y1, 'r--')
ax.plot(x, y2, 'g')
ax.set_title('Exponential Decay of Radioactive Elements')
ax.set_xlabel('Time (years')
ax.set_ylabel('Fraction Remaining')
ax.legend(['C-14', 'Ra-226'])

plt.xlim(0, 20000)
plt.ylim(0, 1.0)
plt.show()
