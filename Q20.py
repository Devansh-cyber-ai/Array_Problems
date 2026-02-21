# Rotate Array to the left by k Positions

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2

k = k % len(arr)
rotated = arr[k:] + arr[:k]

print(rotated)