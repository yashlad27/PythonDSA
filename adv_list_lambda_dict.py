# list comprehensions
numbers = [1,2,3,4,5,6,7,8,9,10]

# square each number
squares = [x**2 for x in numbers]

# square even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]

print(f"Original Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Even Squares: {even_squares}")

# dictionary comprehensions
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dictionary: {square_dict}")

# lambda functions (anonymous functions)
double = lambda x : x * 2
print(f"Double of 5: {double(5)}")

# sorting with lambda
students = [
	{"name": "Alice", "grade": 85},
	{"name":"Bob", "grade": 92},
	{"name":"Charlie", "grade": 78}
]

sorted_students = sorted(students, key=lambda s:s["grade"], reverse=True)

print("students sorted by grade (highest first):")

for student in sorted_students:
	print(f"	{student['name']}: {student['grade']}")