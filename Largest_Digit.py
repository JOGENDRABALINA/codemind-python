def find_largest_digit(number):
    number_str = str(number)
    largest_digit = int(number_str[0])
    for digit in number_str:
        current_digit = int(digit)
        if current_digit > largest_digit:
            largest_digit = current_digit
    
    return largest_digit
if __name__ == "__main__":
    number = int(input())
    largest_digit = find_largest_digit(number)
    print(largest_digit)