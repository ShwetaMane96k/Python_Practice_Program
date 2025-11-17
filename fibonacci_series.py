n=int(input("Enter the numbers of terms in fibonacci series :"))
a,b=0,1
count=0
print("Fibonacci series (Skipping Even Numbers) :")
fibonacci_series=[]
while count<n:
    fibonacci_series.append(a)
    a,b=b,a+b
    count+=1

    for num in fibonacci_series :
        if num%2==0:
            print(num,end=" ")
odd_fib_list=[num for num in fibonacci_series if num%2!=0 ]
print("\n\n List of Odd Fibonacci Numbers :",odd_fib_list)