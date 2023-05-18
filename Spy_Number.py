def is_spy_number(number):
    number_str = str(number)
    digit_sum = 0
    digit_product = 1

    for digit in number_str:
        digit_sum += int(digit)
        digit_product *= int(digit)

    if digit_sum == digit_product:
        return True
    else:
        return False

# Test the program
number = int(input())

if is_spy_number(number):
    print("Spy Number")
else:
    print("Not Spy Number")