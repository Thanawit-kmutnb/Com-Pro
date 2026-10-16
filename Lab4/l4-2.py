#perfect number
def Range_mode():
    print("Perfect Number 1-50")
    for num in range(1,50):
        divisors_sum = 0

        for i in range(1,num):
            if num % i == 0:
                divisors_sum += i

        if divisors_sum == num:
            print(num)

def Number_mode():
    divisors_sum = 0
    num = int(input("Enter a number: "))
    for i in range(1,num):
        if num % i == 0:
            divisors_sum += i

    if divisors_sum == num:
        print("Yes")
    else:
        print("No")

def Select_mode():
    mode = input("Mode (r/n) : ")
    if mode == "r":
        Range_mode()
    elif mode == "n":
        Number_mode()


Select_mode()
