import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure(1, figsize=(4, 3))
ax = fig.add_subplot(111)
ax.set_title('bar_animate_test')
# ax.set_xticks([])  # 注释了这个是能看到变化，要不看不到变化，不对，能看到变化，去了注释吧
# ax.set_yticks([])
ax.set_xlabel('xlable')
N = 5
frames = 50
x = np.arange(1, N + 1)

collection = []
collection.append([i for i in x])
for i in range(frames):
    collection.append([ci + 1 for ci in collection[i]])
print(collection)
xstd = [0, 1, 2, 3, 4]
bars = ax.bar(x, collection[0], 0.30)


def animate(fi):
    # collection=[i+1 for i in x]
    ax.set_ylim(0, max(collection[fi]) + 3)  # 对于问题3，添加了这个
    for rect, yi in zip(bars, collection[fi]):
        rect.set_height(yi)
    # bars.set_height(collection)
    return bars
anim = animation.FuncAnimation(fig, animate, frames=frames, interval=10, repeat=False)
plt.show()
