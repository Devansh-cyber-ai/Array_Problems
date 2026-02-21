# Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)
print("The array is: ", arr)
leader = []
for i in range(size):
    flag = True
    for j in range(i + 1, size):
        if arr[i] <= arr[j]:
            flag = False
            break
    if flag:
        leader.append(arr[i])
        break
print("Leader elements: ", leader)

