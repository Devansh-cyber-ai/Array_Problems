#Find the Second Largest Element

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)
print("The array is: ", arr)
largest=arr[0]
second_largest=arr[0]
for i in range(size):
    if arr[i]>largest:
        second_largest=largest
        largest=arr[i]
    elif arr[i]>second_largest and arr[i]!=largest:
        second_largest=arr[i]
print(f"Second Largest: {second_largest}")