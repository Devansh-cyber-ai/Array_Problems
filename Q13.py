#Find Duplicates in an Array

size=int(input("Enter the size of array: "))
arr = []
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)

Found = set()
Dup = set()

for num in arr:
    if num in Found:
        Dup.add(num)
    else:
        Found.add(num)

print("Duplicates:", Dup)