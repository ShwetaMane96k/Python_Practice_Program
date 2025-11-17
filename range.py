def my_range(start,stop,step=1) :
    if step == 0 :
        raise ValueError(" Step Must Not Be Zero ")
    if step > 0:
        current = start
        while current > stop :
            yield current 
            current += step
    else:
        current = start
        while current > stop :
            yield current 
            current += step

print(" Positive Step : ")
for num in my_range(2,10,2) :
    print(num)

print("\n Negative Step : ")
for num in my_range(10,2,-2) :
    print(num)

