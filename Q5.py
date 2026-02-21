#Count Frequency of Elements

size = int(input("Enter size: "))
arr = [int(input("Enter element: ")) for _ in range(size)]
freq={}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print("Frequency:")
for key, value in freq.items():
    print(key, ":", value)