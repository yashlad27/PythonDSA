x = 10;
name = "leetcode"
pi = 3.14
is_valid = True

# data types: int, float, str, bool
# list tuple set dict

if x>5:
    print("greater")
else:
    print("smaller")

for i in range(5):
    print(i)

count = 0
while count < 3:
    count+=1

# functions:
def add(a,b):
    return a+b

print(add(3,4))

# lists and strings:
nums = [1,2,3]
nums.append(4)
print(nums[0:2])

s="leetcode"
print(s[::-1])

name = "Alice"
age = 28
height = 5.8
is_student = True

print(f"{name} is {age} years old. Type of name: {type(name)}")
print(f"Height: {height} ft. Type of height: {type(height)}")
print(f"Student status: {is_student}. Type: {type(is_student)}")

age_str = str(age)
height_int = int(height)

print(f"Age as string: {age_str}, type: {type(age_str)}")
print(f"Height as integer: {height_int}, type: {type(height_int)}")

# core data structures:
# arrays -> list
# set -> set
# stack -> list with .append() and .pop()
# queue -> collections.deque
# heap -> heapq
# graph/tree -> use classes or dict
