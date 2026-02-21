#Find the Sum of Elements

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)
print("The array is: ", arr)
sum = 0
for i in range(size):
    sum += arr[i]
print(f"Sum: {sum}")