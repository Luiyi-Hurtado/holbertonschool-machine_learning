#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# your code here
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Exponential Decay of C-14')
ax.set_xlabel('Time (years)')
ax.set_ylabel('Fraction Remaining')
ax.set_yscale('log')

plt.xlim(0, 28651)
plt.show()
