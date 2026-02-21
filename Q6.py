#Check if Array is Sorted

size = int(input("Enter size: "))
arr = []
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)
flag=True
for j in range (size-1):
    if arr[j]>arr[j+1]:
        flag=False
        break
if flag == True:
    print("Sorted")
else:    
    print("Not Sorted")