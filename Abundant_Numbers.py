def is_abundant_number(num):
    # Calculate the sum of proper divisors
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)

    # Check if the sum is greater than the number
    return divisor_sum > num

# Test the function
num = int(input())
if is_abundant_number(num):
    print(True)
else:
    print(False)