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
        self.products = {}  # เก็บข้อมูลสต็อกสินค้า {product_id: Product}
        self.cart = []      # ตะกร้าสินค้าสำหรับเก็บรายการที่ลูกค้าเลือกในรอบนั้นๆ

    def add_product(self, product_id: str, name: str, price: float, stock: int):
        self.products[product_id] = Product(name, price, stock)

    def check_stock(self, product_id: str, quantity: int) -> bool:
        # ตรวจสอบว่าสินค้ามีเพียงพอหรือไม่ตาม Flowchart
        if product_id not in self.products:
            print("แจ้งเตือน: ไม่พบรหัสสินค้านี้ในระบบ")
            return False
        
        item = self.products[product_id]
        if item.stock < quantity:
            print(f"แจ้งเตือน: สินค้าไม่พอ/หมดสต็อก (คงเหลือเพียง {item.stock} ชิ้น)")
            return False
            
        return True

    def add_to_cart(self, product_id: str, quantity: int):
        
        #รับข้อมูลการเลือกสินค้าจากลูกค้าและระบุจำนวน
        #บันทึกรายการสินค้าลงตะกร้าหากสต็อกเพียงพอ
        
        if self.check_stock(product_id, quantity):
            product = self.products[product_id]
            subtotal = product.price * quantity
            
            # บันทึกรายการลงตะกร้า
            self.cart.append({
                'product_id': product_id,
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'subtotal': subtotal
            })
            print(f"บันทึกรายการสำเร็จ: {product.name} x {quantity} ชิ้น ({subtotal:.2f} บาท)")

    def display_cart_and_total(self) -> float:
        # แสดงรายการสินค้าทั้งหมดในตะกร้าและคำนวณราคารวม
        print("\n=== รายการสินค้าที่เลือกทั้งหมด ===")
        if not self.cart:
            print("ไม่มีรายการสินค้าในตะกร้า")
            return 0.0
            
        total_price = 0.0
        for idx, item in enumerate(self.cart, 1):
            print(f"{idx}. {item['name']} x {item['quantity']} ชิ้น - {item['subtotal']:.2f} บาท")
            total_price += item['subtotal']
            
        print("-----------------------------------")
        print(f"ราคารวมทั้งหมด: {total_price:.2f} บาท")
        print("===================================")
        return total_price

    def show_all_products(self):
        # แสดงรายการสินค้าทั้งหมดในระบบ
        print("\n=== รายการสินค้าในระบบ ===")
        for p_id, item in self.products.items():
            print(f"[{p_id}] {item}")
        print("==========================")


# ส่วนการทดสอบโค้ดประจำสัปดาห์ที่ 2

if __name__ == "__main__":
    app = Cashier()

    # 1. รับข้อมูลลิสต์สินค้าตั้งต้น
    app.add_product("P01", "น้ำดื่ม", 10.0, 50)
    app.add_product("P02", "ขนมปัง", 25.0, 20)
    app.add_product("P03", "กาแฟ", 45.0, 5)  # กาแฟมีสต็อกแค่ 5 ชิ้น

    app.show_all_products()

    # 2. จำลองการเลือกสินค้าและระบุจำนวนของลูกค้า
    print("\n--- ทดสอบการเลือกสินค้า ---")
    app.add_to_cart("P01", 2)   # ซื้อ น้ำดื่ม 2 ชิ้น (ผ่าน)
    app.add_to_cart("P03", 10)  # ซื้อ กาแฟ 10 ชิ้น (สต็อกไม่พอ -> แสดงแจ้งเตือน)
    app.add_to_cart("P03", 3)   # ซื้อ กาแฟ 3 ชิ้น (ผ่าน)

    # 3. แสดงรายการสินค้าเล่าและราคารวม
    app.display_cart_and_total()