#Remove Duplicates from Array: Remove duplicates from the array while maintaining order.

size=int(input("Enter the size of array: "))
arr=[]
for i in range(size):
    element=int(input("Enter element: "))
    arr.append(element)    
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)