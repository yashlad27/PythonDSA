# find the maximum in a list

def max_in_list(arr):
    max_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

print(max_in_list([2, 5, 1, 9, 7]))