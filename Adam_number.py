def is_adam_number(number):
    square = number ** 2
    reverse = int(str(number)[::-1])
    reverse_square = reverse ** 2
    reverse_of_square = int(str(reverse_square)[::-1])
    return square == reverse_of_square
if __name__ == "__main__":
    number = int(input())
    if is_adam_number(number):
        print(True)
    else:
        print(False)