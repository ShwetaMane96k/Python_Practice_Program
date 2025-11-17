def count_occurence(tup):
    occurrence={}
    for item in tup :
        if item in occurrence :
            occurrence[item]+=1
        else:
            occurrence[item]=1
        return occurrence
tup=(1,2,3,4,5,6,7,8,7,6,5,4,3,2,2,1,0,7,3)
print(count_occurence(tup))