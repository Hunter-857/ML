import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x = np.arange(0, 5)
y = 50 * x
# # 绘制1
plt.plot(x, y, 'r-')
plt.legend(loc='lower right')
plt.xlabel(xlabel="time/h")
plt.ylabel(ylabel="distance/km")
plt.xlim((0, 5))
plt.ylim((0, 250))
plt.grid()
plt.show()
plt.savefig("speed.png")