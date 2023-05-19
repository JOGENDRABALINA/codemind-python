def is_ugly(number):
    if number <= 0:
        return False
    while number % 2 == 0:
        number //= 2
    while number % 3 == 0:
        number //= 3
    while number % 5 == 0:
        number //= 5
    return number == 1

if __name__ == "__main__":
    number = int(input())
    if is_ugly(number):
        print("Ugly Number")
    else:
        print("Not Ugly Number")