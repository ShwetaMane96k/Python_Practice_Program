def find_pairs(numbers ,target_sum):
    pairs=[]
    n=len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            if numbers[i]+numbers[j]==target_sum:
                pairs.append((numbers[i],numbers[j]))
                return pairs
nums=[2,4,3,5,7,8,9,1]
target=10
print("Pairs with sum", target,":",find_pairs(nums,target))
