'''
dictionary comprehensions provide an elegant way to create
dictionaries using a single line of code. They follow 
a similar syntax to list comprehensions but use curly braces 
and include both a key and value expression.
'''

# create a dictionary from two lists
names = ["alice", "bob", "charlie"]
ages = [25, 30, 22]
name_to_age = {name: age for name, age in zip(names, ages)}
print(f"Name to age mapping: {name_to_age}")

# transforming keys and values from another dict
original = {"a":1, "b":2, "c":3}
uppercase_dict = {k.upper(): v**2 for k, v in original.items()}
print(uppercase_dict)

# dictionary comprehension with nested loops:
matrix_positions = {(i,j): i*j 
						for i in range(1,4) for j in range(1,4)}
print(f"matrix_positions: {matrix_positions}")