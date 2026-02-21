#Rotate Array by k Positions: Rotate the array to the right by k positions.

size = int(input("Enter size: "))
arr = [int(input("Enter element: ")) for _ in range(size)]
k = int(input("Enter k: "))
k = k % size
rotated = arr[size-k:] + arr[:size-k]
print("Rotated array:", rotated)