# Find Peak Element: A peak element is greater than its neighbors. Find one such element.

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)
print("The array is: ", arr)
for i in range(size):
    if (i == 0 or arr[i] >= arr[i - 1]) and (i == size - 1 or arr[i] >= arr[i + 1]):
        print(f"Peak Element: {arr[i]}")
        break
