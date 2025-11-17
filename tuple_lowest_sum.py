def tuple_with_lowest_sum(tuple_list):
    if not tuple_list:
        return None
        return min(tuple_list,key=sum)
tuple=[(3,4,1),(2,2,2),(5,1),(0,1,0)]
print("List of Tuples :",tuple)
print("Tuples with lowest sum :",tuple_with_lowest_sum(tuple))