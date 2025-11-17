def rotate_list(list,n):
    n=n%len(list)
    rotated=list[-n:]+list[:-n]
    return rotated
numbers=[1,2,3,4,5,6,7,8,9]
n=2
print("Original List :",numbers)
print("List after rotating by",n,"position :",rotate_list(numbers,n))