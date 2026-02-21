# Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.

size=int(input("Enter the size of array: "))
arr=[]
for i in range(size):
    element=int(input("Enter element: "))
    arr.append(element)
print("The array is: ",arr)
non_zero_index=0
for i in range(size):
    if arr[i]!=0:
        arr[non_zero_index]=arr[i]
        non_zero_index+=1
for i in range(non_zero_index,size):
    arr[i]=0
print("Array after moving zeroes to the end: ",arr)
