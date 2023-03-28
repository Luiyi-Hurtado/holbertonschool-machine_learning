#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
fig, ax = plt.subplots()
ax.hist(student_grades, bins=[40, 50, 60, 70, 80, 90, 100], edgecolor='black')
ax.set_title('Project A')
ax.set_xlabel('Number of Students')
ax.set_ylabel('Grades')

plt.xlim(0, 100)
plt.ylim(0, 30)
plt.show()
