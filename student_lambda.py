students = [
    ("Aarav", 21, 85),
    ("Saanvi", 22, 92),
    ("Rohan", 20, 76),
    ("Isha", 23, 88),
    ("Kabir", 21, 67)
]

# 1. Sort students by Marks using lambda
sorted_by_marks = sorted(students, key=lambda x: x[2], reverse=True)

print("Students sorted by Marks (High → Low):")
for s in sorted_by_marks:
    print(s)

# 2. Filter students who scored more than 80
top_students = list(filter(lambda x: x[2] > 80, students))
print("\nStudents with Marks > 80:", top_students)

# 3. Map: Extract just names in uppercase
names_upper = list(map(lambda x: x[0].upper(), students))
print("\nNames in Uppercase:", names_upper)

# 4. Reduce: Find total marks of all students
from functools import reduce
total_marks = reduce(lambda a, b: a + b[2], students, 0)
print("\nTotal Marks of all students:", total_marks)

# 5. Nested lambda: Function to create multiplier
multiplier = lambda n: (lambda x: x * n)
double = multiplier(2)
triple = multiplier(3)
print("\nDouble of 10:", double(10))
print("Triple of 10:", triple(10))
