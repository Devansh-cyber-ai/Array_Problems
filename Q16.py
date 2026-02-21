# Check if Two Arrays Are Equal: if two arrays contain the same elements

arr1 = [1, 2, 2, 3]
arr2 = [2, 1, 3, 5]

if len(arr1) != len(arr2):
    print("Not equal")
else:
    freq = {}
    
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in arr2:
        if num not in freq or freq[num] == 0:
            print("Not equal")
            break
        freq[num] -= 1
    else:
        print("Arrays are equal")