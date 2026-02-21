#Find Intersection of Two Arrays: Find the common elements between two arrays.

arr1=[1,2,3,4,5]
arr2=[4,5,6,7,8]
common=[]
for i in arr1:
    if i in arr2:
        common.append(i)
print(common)
