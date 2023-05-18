def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(number):
    temp = number
    digit_sum = 0
    while temp > 0:
        digit = temp % 10
        digit_sum += factorial(digit)
        temp //= 10
    if digit_sum == number:
        return True
    else:
        return False

# Test the program
number = int(input())

if is_strong_number(number):
    print('The number',number, "is a strong number")
else:
    print('The number',number, "is not a strong number")