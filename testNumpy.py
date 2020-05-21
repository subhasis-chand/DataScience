import numpy as np

arr = np.array([1,2,3,4,5])
print("arrayis :", arr)
print("type of arr: ", type(arr))

arr2 = np.array([[1,2,3,4], [5,6,7,8]])
print("2d arr is: \n", arr2)

arr2 = np.append(arr2, [1,3,6, 8])
print("2d arr is: \n", arr2)
# append in np is different from append in list

arr2 = np.array([[1,2,3,4], [5,6,7,8], [1,4,6,7]])
print("2d arr is: \n", arr2)

print("shape of array: ", arr2.shape)
print(arr2[1,2])
print(arr2[1])
print(arr2[1][2])

arr2[1][2] = 0
print(arr2)

arr0 = np.zeros((3,6))
print(arr0)

arrOnes = np.ones((7,10))
print(arrOnes)

slc = arr2[ 0:2 , 0:2 ]
print(slc)

arrOnesCopy = arrOnes

arrOnesCopy[0][0] = 10
print("copy : \n", arrOnesCopy)
print("actual : \n", arrOnes)

arrOnesCopy2 = np.copy(arrOnes)
arrOnesCopy2[1][1] = 10
print("copy2 : \n", arrOnesCopy2)
print("actual : \n", arrOnes)

print("data type of arr2: ", arr2.dtype)

arr3 = np.array([[1,2,3],[4,5,6]], dtype="float")
print("data type of arr3: ", arr3.dtype)

print("arr3: \n", arr3)
arr3[arr3 < 5] = 0
print("arr3: \n", arr3)

arr3 = np.array([[1,2,3],[4,5,6]], dtype="float")
arr3[arr3 % 2 == 0] = 10
print("arr3: \n", arr3)

mask = np.array([[True, False, True], [True, True, True]])
print('mask: \n', mask)
arr3[mask] = 100
print("arr3: \n", arr3)

arr3[mask == False] = 9.8
print("arr3: \n", arr3)

npStr = np.array(["abc", "def", "xyz"])
print("numpy string: \n", npStr)

npDots = np.ones((4,5)) * 5
print("npdots : \n", npDots)

print("shape of npDots: ", npDots.shape)
newArr = npDots.reshape(20)
print("one d converted arr: \n", newArr)

convert2D = newArr.reshape(2, 10)
print("two d converted arr: \n", convert2D)

print(convert2D.T)

arangeExampleArr = np.arange(20)
print("arange example: \n", arangeExampleArr)

arangeExampleArr.shape = (5,4)
print("arange example: \n", arangeExampleArr)
arangeExampleArr = arangeExampleArr.reshape(-1)
print("arange example: \n", arangeExampleArr)

arangeExampleArr = np.arange(15, 60, 4)
print("arange example: \n", arangeExampleArr)

arangeExampleArr = np.arange(20)
arangeExampleArr.shape = (5,4)
print("arange example: \n", arangeExampleArr)

print("mul by 5: \n", arangeExampleArr * 5)
print("square all elements: \n", arangeExampleArr ** 2)
print("square all elements: \n", np.square(arangeExampleArr))

arr1 = np.array([[1,2,3], [4,5,6]])
arr2 = np.array([[7,8,9], [3,5,7]])
print("addition of arr: \n", arr1 + arr2)
print("mul of arr: \n", arr1 * arr2)

mat1 = np.matrix([[1,2,3], [4,5,6]])
mat2 = np.matrix([[7,8,9], [3,5,7]])

print("matrix: \n", mat1,"\n", mat2)
print(type(mat1))
print("transpose of mat2: \n", mat2.T)
print("mul of mat: \n", mat1 * mat2.T)
print("square all elements: \n", np.square(mat1))
print("pow3 all elements: \n", np.power(mat1, 3))



import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)
plt.show()























