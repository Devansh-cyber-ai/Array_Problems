#Reverse an Array

size=int(input("Enter the size of array: "))
arr=[]
for i in range(size):
    arr.append(int(input("Enter the element: ")))
print("The array is: ",arr)
print("Reversed array: ",end="")
rarr=[]
for i in range(len(arr)-1,-1,-1):
    rarr.append(arr[i])
print(rarr)