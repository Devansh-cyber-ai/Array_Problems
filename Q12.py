#Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

size=int(input("Enter the size of the array: "))
arr=[]
for i in range(size):
    element=int(input("Enter element: "))
    arr.append(element)
print(arr)
expected_sum = (len(arr)+1) * (len(arr) + 2) // 2
actual_sum = sum(arr)

missing = expected_sum - actual_sum
print("Missing number:", missing)
