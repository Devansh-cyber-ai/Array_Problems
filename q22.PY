# Find All Subarrays

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)
print("The array is: ", arr)

n = len(arr)

for i in range(n):
    for j in range(i, n):
        print(arr[i:j+1])