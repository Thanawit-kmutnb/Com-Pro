class Product:
    #Class สำหรับเก็บข้อมูลสินค้าแต่ละรายการ
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ราคา: {self.price:.2f} บาท | คงเหลือ: {self.stock} ชิ้น"


class Cashier:
    #Class หลักสำหรับควบคุมระบบแคชเชียร์และคลังสินค้า
    def __init__(self):
        self.products = {}

    def add_product(self, product_id: str, name: str, price: float, stock: int):
        # เพิ่มสินค้าใหม่เข้าสู่ระบบ
        self.products[product_id] = Product(name, price, stock)

    def check_stock(self):
        # แสดงรายการสินค้าและจำนวนคงเหลือทั้งหมดในสต็อก
        print("\n=== รายการสินค้าและสต็อกคงเหลือ ===")
        if not self.products:
            print("ไม่มีสินค้าในระบบ")
            return
        
        for p_id, item in self.products.items():
            print(f"[{p_id}] {item}")
        print("===================================")



# ทดสอบโค้ดประจำสัปดาห์ที่ 1

app = Cashier()

# รับข้อมูลลิสต์สินค้าตั้งต้น (ชื่อ, ราคา, สต็อก) ตาม Flowchart
app.add_product("P01", "น้ำดื่ม", 10.0, 50)
app.add_product("P02", "ขนมปัง", 25.0, 20)
app.add_product("P03", "กาแฟ", 45.0, 15)

# ทดสอบฟังก์ชันเช็กสต็อก
app.check_stock()