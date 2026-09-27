# ระบบตัดสต็อกสินค้าและบันทึกข้อมูลกลับลงไฟล์
class Product:
    def __init__(self, item_id, name, price, stock):
        self.item_id = item_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def sell(self, amount):
        if amount <= self.stock:
            self.stock -= amount
            print(f"ขาย {self.name} จำนวน {amount} ชิ้นสำเร็จ! (คงเหลือ: {self.stock})")
            return True
        else:
            print(f"สินค้า {self.name} มีไม่พอในสต็อก (คงเหลือเพียง {self.stock})")
            return False

    def to_file_format(self):
        return f"{self.item_id},{self.name},{self.price},{self.stock}\n"

# ฟังก์ชันอ่านข้อมูลในไฟล์
def load_inventory(file_path):
    products = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                item_id, name, price, stock = line.split(",")
                products.append(Product(item_id, name, price, stock))
    return products

# ฟังก์ชันบันทึกข้อมูลกลับลงไฟล์
def save_inventory(file_path, products):
    with open(file_path, "w", encoding="utf-8") as file:
        for p in products:
            file.write(p.to_file_format())
    print("บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว!")


file_path = "Lab8/Lab8-5/inventory.txt"
# อ่านข้อมูลสินค้า
inventory = load_inventory(file_path)

# ทดสอบตัดสต็อกสินค้า
if inventory:
    print("=== ก่อนการตัดสต็อก ===")
    print(f"สินค้า: {inventory[0].name} | คงเหลือ: {inventory[0].stock}")
    
    print("\n--- ทำรายการขาย ---")
    inventory[0].sell(5)

    save_inventory(file_path, inventory)


