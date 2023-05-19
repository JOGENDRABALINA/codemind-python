def is_unique_number(number):
    number_str = str(number)
    return len(set(number_str)) == len(number_str)
if __name__ == "__main__":
    number = int(input())
    if is_unique_number(number):
        print("Unique Number")
    else:
        print("Not Unique Number")