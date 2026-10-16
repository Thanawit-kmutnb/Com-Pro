def calculate_area(width, length):
    return width * length

def volleyball(area):
    return area >= 162

def basketball(area):
    return area >= 420

def football(area):
    return area >= 4050

print("=== โปรแกรมคำนวณพื้นที่ดินสำหรับจัดแข่งขันกีฬา ===")
width = float(input("กรุณากรอกความกว้าง (เมตร): "))
length = float(input("กรุณากรอกความยาว (เมตร): "))

land_area = calculate_area(width, length)

print(f"\ื้นที่ดินทั้งหมด: {land_area:,.2f} ตารางเมตร")
print("กีฬาที่สามารถจัดแข่งขันได้:")

if volleyball(land_area):
    print("- Volleyball")
if basketball(land_area):
    print("- Basketball")
if football(land_area):
    print("- Football")

if not volleyball(land_area):
    print("- ไม่สามารถจัดแข่งขันกีฬาข้างต้นได้เนื่องจากพื้นที่ไม่เพียงพอ")