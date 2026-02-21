#Remove given Element from Array

arr=[]
size=int(input("Enter the size of array: "))
for i in range (size):
    element=int(input("Enter element: "))
    arr.append(element)
print(f"Array: {arr}")
target=int(input("Enter the element to be removed: "))
while target in arr:
    arr.remove(target)
print(arr)