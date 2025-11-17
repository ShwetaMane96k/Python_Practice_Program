def find_even_numbers(numbers):
    even_numbers = [num for num in numbers if num%2==0]
    return even_numbers
num=[10,15,20,25,30,35,40,45]
print("Even Numbers :",find_even_numbers(num))