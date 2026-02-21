# Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.

size=int(input("Enter the size of array: "))
arr=[]
for i in range(size):
    element=int(input("Enter element: "))
    arr.append(element)

arr.sort()
result = []

left = 0
right = len(arr) - 1

while left <= right:
    if left != right:
        result.append(arr[right])
        result.append(arr[left])
    else:
        result.append(arr[left])
    left += 1
    right -= 1

print(result)