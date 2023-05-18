import math

def is_perfect_square(num):
   
    square_root = math.isqrt(num)
    return square_root * square_root == num

number = int(input())
if is_perfect_square(number):
    print(True)
else:
    print(False)