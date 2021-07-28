import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')  # 画线并添加图例legend
plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')  # 画线并添加图例legend
plt.legend()  # 展示图例legend
plt.xlabel('Rads')  # 给 x 轴添加坐标轴信息
plt.ylabel('Amplitude')  # 给 y 轴添加坐标轴信息
plt.title('Sin and Cos Waves')  # 添加图片标题
# plt.axis('off')   # 关闭坐标轴的显示
plt.show()
