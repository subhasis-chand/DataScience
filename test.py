a = [1,3,2,6,4,5]

for i in range(len(a)):
    print(a[i])

a = sorted(a)

print(a)
a.reverse()
print(a)

a.append(10)
print("appended 10 to the list: ", a)

a.insert(1,11)
print("inserted 11 at index 1: ", a)