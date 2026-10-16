#BMI
def cal_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif bmi >= 30:
        return "Obesity"


def main():
    weight = float(input("enter weight(kg): "))
    height = float(input("enter height(m): "))

    bmi = cal_bmi(weight, height)
    category = bmi_category(bmi)

    print("----------------------------------------")
    print(f"ค่า BMI ของคุณ: {bmi:.2f}")
    print(f"Weight Status: {category}")

main()