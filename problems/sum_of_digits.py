# sum of digits:
# input : 1234
# 1+2+3+4 = 10
# return sum

def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n%10
        total += digit
        n = n//10
    return total

print(sum_of_digits(1234))