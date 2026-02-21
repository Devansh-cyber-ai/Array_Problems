# Find union of two arrays

arr1=[1,2,3,4,5]
arr2=[4,5,3,4,7,9]
union=[]
for i in arr1:
    if i not in union:
        union.append(i)
for i in arr2:
    if i not in union:
        union.append(i)
print(union)
