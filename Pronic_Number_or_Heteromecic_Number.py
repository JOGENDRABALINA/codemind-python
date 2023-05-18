def is_pronic_number(number):
    sqrt = int(number ** 0.5)  
    if sqrt * (sqrt + 1) == number:
        return True
    else:
        return False

# Test the program
number = int(input())

if is_pronic_number(number):
    print("YES")
else:
    print("NO")