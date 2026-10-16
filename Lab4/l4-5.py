#change coins
while True:
    money = int(input("\nEnter amount (0 to exit): "))
    if money == 0:
        print("Exiting program.")
        break

    b10 = money // 10
    remainder = money % 10

    b5 = remainder // 5
    b1 = remainder % 5

    print(f"เหรียญ 10 จำนวน {b10} เหรียญ")
    print(f"เหรียญ 5 จำนวน {b5} เหรียญ")
    print(f"เหรียญ 1 จำนวน {b1} เหรียญ")