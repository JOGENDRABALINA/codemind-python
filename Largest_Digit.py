def find_largest_digit(num):
    
    num_str = str(num)
    max_digit = 0
    for digit in num_str:
        if int(digit) > max_digit:
            max_digit = int(digit)
    return max_digit


number = int(input())
largest_digit = find_largest_digit(number)

print(largest_digit)