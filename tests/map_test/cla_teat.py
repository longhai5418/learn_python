import matplotlib.pyplot as plt
import numpy as np

# np.random.seed(19680801)
# data = np.random.random((6, 3, 4))
# print(data)
# fig, ax = plt.subplots()
#
# for i in range(len(data)):
#     ax.cla()
#     ax.imshow(data[i])
#     ax.set_title("frame {}".format(i))
#     plt.pause(0.1)

# data_X = np.random.randint(33, size=50)
# data_Y = np.random.randint(20, size=50)
# print(data_X)
# print(data_Y)

# plt.figure(figsize=(15, 8), dpi=100)
# plt.bar(data_X, data_Y, width=0.5)
# plt.show()
for i in range(3):
    data_X = np.random.randint(33, size=50)
    data_Y = np.random.randint(20, size=50)
    plt.figure(figsize=(15, 8), dpi=100)
    plt.bar(data_X, data_Y, width=0.5)
    plt.pause(0.3)

