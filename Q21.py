# Find the Kth Smallest Element

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)
print("The array is: ", arr)
k = int(input("Enter the value of k: "))
arr.sort()
if k <= size:
    print(f"{k}th Smallest Element: {arr[k-1]}")
else:
    print("k is greater than the size of the array.")
