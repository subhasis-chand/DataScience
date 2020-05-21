import matplotlib.pyplot as plt
import numpy as np

# y = [1,3,2,5,7,4,8,10]
# x = [2,4,5,7,9,10,13,14]

# plt.plot(x,y, 'x-g')
# # plt.show()

# x1 = [1,2,3,4,5,6,7]
# plt.plot(x1, '.-r')
# plt.show()

# for i in range(10):
#     plt.cla()
#     x = np.random.randint(1, 20, 10)
#     plt.plot(x, '.-')
#     plt.pause(1)
# plt.show()
##################################################
# temp = []
# for i in range(12):
#     plt.cla()
#     hourlyTemp = np.random.randint(30,35,1)
#     temp.append(hourlyTemp[0])
#     plt.plot(temp, '.-r')
#     plt.pause(1)
# plt.show()

#####################################################

# sinCurve = []
# for x in range(700):
#     plt.cla()
#     # x * pi/180 rad = x deg
#     y = np.sin(x * np.pi / 180.0)
#     sinCurve.append(y)
#     plt.plot(sinCurve)
#     plt.pause(0.05)

######################################################


# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)

# fig, axs = plt.subplots(2)
# fig.suptitle('Vertically stacked subplots')
# axs[0].plot(x, y)
# axs[1].plot(x, -y)
# plt.show()

####################################################

# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)

# fig, axs = plt.subplots(1, 2)
# print(axs, type(axs), axs.shape)
# fig.suptitle('Vertically stacked subplots')
# axs[0].plot(x, y)
# axs[1].plot(x, -y)
# plt.show()

#####################################################

# x = np.linspace(0, 2 * np.pi, 400)
# y1 = np.sin(x ** 2)
# y2 = np.cos(x ** 2)

# fig, axs = plt.subplots(2, 2)
# axs[0,0].plot(x, y1, 'r')
# axs[0,1].plot(x, -y1, 'g')
# axs[1,0].plot(x, y2, 'b')
# axs[1,1].plot(x, -y2, 'k')
# plt.show()

#######################################################

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='edge', alpha=1, width=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()