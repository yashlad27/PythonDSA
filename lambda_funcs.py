#basic
double = lambda x:x*2
print(f"Double of 5: {double(5)}")

# lambda with multiple args
add = lambda x,y:x+y
print(f"3+4={add(3,4)}")

# using lambdas with built in functions like a map
numbers = [1,2,3,4,5]
squared = list(map(lambda x:x**2, numbers))
print(f"Squared numbers: {squared}")

# using lambdas with filters
even_numbers = list(filter(lambda x:x%2==0, numbers))
print(f"even numbers: {even_numbers}")