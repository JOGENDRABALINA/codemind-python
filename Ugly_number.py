def is_ugly_number(num):
    
    if num <= 0:
        return False
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    return num == 1

number = int(input())
if is_ugly_number(number):
    print("Ugly Number")
else:
    print("Not Ugly Number")