def reverse_integer(num):
   
    reversed_num = 0
    is_negative = False

    if num < 0:
        is_negative = True
        num = -num

    while num != 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10

    if is_negative:
        reversed_num = -reversed_num

    return reversed_num


number = int(input())
reversed_number = reverse_integer(number)

print( reversed_number)