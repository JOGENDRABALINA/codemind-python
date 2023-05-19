def reverse_number(number):
    reversed_str = str(number)[::-1]
    reversed_number = int(reversed_str)
    
    return reversed_number

if __name__ == "__main__":
    number = int(input())
    reversed_number = reverse_number(number)
    print( reversed_number)