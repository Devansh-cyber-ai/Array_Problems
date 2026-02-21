# Find the First Missing Positive: Find the smallest positive integer missing in the array.

size=int(input("Enter the size of the array: "))
arr=[]
for i in range(size):
    element=int(input("Enter element: "))
    arr.append(element)
print(arr)
for i in range(1, size + 1):
    if i not in arr:
        print("The smallest positive integer missing is:", i)
        break
