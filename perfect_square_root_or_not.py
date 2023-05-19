import math

def is_perfect_square(number):
    square_root = math.isqrt(number)
    return square_root * square_root == number

if __name__ == "__main__":
    number = int(input())
    if is_perfect_square(number):
        print(True)
    else:
        print(False)