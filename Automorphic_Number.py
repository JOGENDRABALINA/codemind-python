def is_automorphic_number(number):
    square = number ** 2
    square_str = str(square)
    number_str = str(number)
    if square_str.endswith(number_str):
        return True
    else:
        return False

# Test the program
number = int(input())

if is_automorphic_number(number):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")