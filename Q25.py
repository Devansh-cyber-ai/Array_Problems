# Find Majority Element: Find the element that appears more than n/2 times.

arr = [2,2,1,1,2,2,2]

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1
    if freq[i] > len(arr)//2:
        print("Majority element:", i)
        break