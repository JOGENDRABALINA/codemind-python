def is_happy_number(number):

    seen_numbers = set()
    while number != 1:
        if number in seen_numbers:
            return False
        seen_numbers.add(number)
        next_number = 0
        while number > 0:
            digit = number % 10
            next_number += digit * digit
            number //= 10
        
        number = next_number
    
    return True
if __name__ == "__main__":
    number = int(input())
    if is_happy_number(number):
        print(True)
    else:
        print(False)






