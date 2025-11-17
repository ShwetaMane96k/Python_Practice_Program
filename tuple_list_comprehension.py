numbers=[int(input(f"Enter Numbers {i+1}:"))for i in range(10)]
unique_even=tuple({num for num in numbers if num%2==0})
odd_cubes=[num**3 for num in numbers if num%2!=0]
print("\n --------Result---------")
print(f"Unique Even Numbers (Tuple) :{unique_even}")
print(f"Odd Cubes Numbers (List) :{odd_cubes}")