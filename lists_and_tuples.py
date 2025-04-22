fruits = ["apple", "banana", "cherry", "orange"]

print(f"Original List: {fruits}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"First 3 items: {fruits[:3]}")
print(f"List length: {len(fruits)}")

fruits.append("grape")  # add to the end
fruits.insert(1, "blueberry")   # insert at position
removed_fruit = fruits.pop(2)		# remove and return item

print(f"Updated list: {fruits}")
print(f"Removed fruit: {removed_fruit}")


# tuples : immutable ordered collections
coordinates = (10,20)
x, y = coordinates  # tuple unpacking
print(f"Coordinates: {coordinates}, X: {x}, Y: {y}")

# trying to modify a tuple will cause an error
# coordinates[0] = 15 will raise "TypeError"!