#Find the Maximum & Minimum Element

size=int(input("Enter the size of array: "))
arr=[]
for i in range(size):
    arr.append(int(input("Enter the element: ")))
print("The array is: ",arr)
max=arr[0]
min=arr[0]
for i in range(1,size):
    if arr[i]>max:
        max=arr[i]
print(f"Maximum element: {max}")
for i in range(1,size):
    if arr[i]<min:
        min=arr[i]
print(f"Minimum element: {min}")