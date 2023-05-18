def is_neon_number(number):
    square = number ** 2
    digit_sum = sum(int(digit) for digit in str(square))
    if digit_sum == number:
        return True
    else:
        return False

# Test the program
number = int(input())

if is_neon_number(number):
    print("Neon Number")
else:
    print("Not Neon Number")