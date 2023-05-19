def calculate_lcm(num1, num2):
    greater = max(num1, num2)
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1
    
    return lcm
if __name__ == "__main__":
    a,b=map(int,input().split())
    lcm = calculate_lcm(a,b)
    print(lcm)




