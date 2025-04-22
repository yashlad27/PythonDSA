# dictionaries -> key-value pairs
student = {
	"name":"Bob",
	"age":21,
	"courses":["Math", "CS", "Phy"],
	"active":True
}

# access and modify dictionaries:
print(f"Student name: {student['name']}")
print(f"Courses: {student['courses']}")

# adding and modifying entries
student["gpa"] = 3.8
student["age"] = 22
print(f"Updated Student: {student}")

# dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# get with default values (prevents KeyError)
major = student.get("major", "Undeclared")
print(f"Major: {major}")

# sets - unordered collections of unique elements
courses_a = {"Math", "Phy", "Chem"}
courses_b = {"CS", "Math", "Statistics"}

# set operations

# union (all unique elements)
union = courses_a | courses_b

# intersection (Common elements)
intersection = courses_a & courses_b 

# Difference (in A but not in B)
difference = courses_a - courses_b

print(f"All courses: {union}")
print(f"common courses: {intersection}")
print(f"courses in A but not in B: {difference}")

