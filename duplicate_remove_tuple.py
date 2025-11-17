def remove_duplicate(tup):
    unique_tup=tuple(dict.fromkeys(tup))
    return unique_tup
tup=(1,2,3,4,5,1,2,3,4,5,6,3,6,4,5)
print("Original Tuple :",tup)
print("Tuple after removing duplicates :",remove_duplicate(tup))