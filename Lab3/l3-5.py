def cal_premium(base_price, age, smoke, disease):
    if base_price <= 0 or not (1 <= age <= 100):
        return "Error: ราคาหรืออายุไม่ถูกต้อง"

    if age < 30:
        premium = base_price
    elif age <= 59:
        premium = base_price * 1.2
    else:
        premium = base_price * 1.5

    if smoke and disease:
        premium *= 1.3
    elif smoke or disease:
        premium *= 1.15

    return premium

price_in = float(input("กรอกเบี้ยพื้นฐาน: "))
age_in = int(input("กรอกอายุ: "))
smoke_in = input("สูบบุหรี่หรือไม่ (y/n): ").lower() == 'y'
disease_in = input("มีโรคประจำตัวหรือไม่ (y/n): ").lower() == 'y'

result = cal_premium(price_in, age_in, smoke_in, disease_in)
print("ยอดเบี้ยประกันสุทธิ:", round(result))

