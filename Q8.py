#Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

size = int(input("Enter size: "))
arr = [int(input("Enter element: ")) for _ in range(size)]
target = int(input("Enter target sum: "))
seen = set()
found = False

for num in arr:
    need = target - num
    if need in seen:
        print("Pair found:", need, "+", num, "=", target)
        found = True
        break
    seen.add(num)

if not found:
    print("No pair found")