balance = 10000  # ยอดเงินเริ่มต้นในบัญชี

while True:
    print(f"\n--- ATM Machine (Current Balance: {balance} THB) ---")
    amount = int(input("Enter withdrawal amount (0 to exit): "))

    if amount == 0:
        print("Thank you for using our service.")
        break

    if amount > balance:
        print("Error: Insufficient funds!")
    elif amount % 100 != 0:
        print("Error: Amount must be a multiple of 100!")
    else:
        balance -= amount

        b1000 = amount // 1000
        remainder = amount % 1000

        b500 = remainder // 500
        remainder %= 500

        b100 = remainder // 100

        print("--- Dispensing Banknotes ---")
        print(f"1000 THB Note : {b1000}")
        print(f" 500 THB Note : {b500}")
        print(f" 100 THB Note : {b100}")
