class Product:
    #Class สำหรับเก็บข้อมูลสินค้าแต่ละรายการ (name, price, stock)
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name:<15} | ราคา: {self.price:>7.2f} บาท | คงเหลือ: {self.stock:>4} ชิ้น"


class Cashier:
    #Class หลักควบคุมการคิดเงิน ทอนเงิน และตัดสต็อกลงไฟล์ .txt
    def __init__(self, filename: str = "products.txt"):
        self.filename = filename
        self.products = {}  # เก็บข้อมูลสินค้า {product_id: Product}
        self.cart = []      # ตะกร้าสินค้าลูกค้ารายปัจจุบัน

    def load_products_from_file(self) -> bool:
        #อ่านข้อมูลสินค้าและสต็อกจากไฟล์ products.txt
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                self.products.clear()
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # ข้ามบรรทัดว่าง
                    
                    parts = line.split(',')
                    if len(parts) == 4:
                        p_id = parts[0].strip().upper()
                        name = parts[1].strip()
                        price = float(parts[2].strip())
                        stock = int(parts[3].strip())
                        self.products[p_id] = Product(name, price, stock)
            return True

        except FileNotFoundError:
            print(f"\nไม่พบไฟล์ '{self.filename}'!")
            print(f"กรุณาสร้างไฟล์ '{self.filename}' ไว้ในโฟลเดอร์เดียวกันก่อนเริ่มใช้งานโปรแกรม")
            return False
            
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการอ่านไฟล์ '{self.filename}': {e}")
            return False

    def save_products_to_file(self):
        #อัปเดตสต็อกสินค้าล่าสุดกลับลงไฟล์ .txt
        try:
            with open(self.filename, mode='w', encoding='utf-8') as file:
                for p_id, item in self.products.items():
                    file.write(f"{p_id},{item.name},{item.price},{item.stock}\n")
            print(f"อัปเดตสต็อกลงไฟล์ '{self.filename}' เรียบร้อยแล้ว")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")

    def check_stock(self):
        #เช็กสินค้าและจำนวนสต็อกทั้งหมดในระบบ
        print("\n================ รายการสินค้าและสต็อกคงเหลือ ================")
        if not self.products:
            print("ไม่มีสินค้าในระบบ")
        else:
            for p_id, item in self.products.items():
                print(f"[{p_id}] {item}")
        print("==========================================================")

    def is_stock_available(self, product_id: str, quantity: int) -> bool:
        #ตรวจสอบว่าสินค้ามีเพียงพอหรือไม่
        if product_id not in self.products:
            print("แจ้งเตือน: ไม่พบรหัสสินค้านี้ในระบบ")
            return False
            
        item = self.products[product_id]
        if item.stock < quantity:
            print(f"แจ้งเตือน: สินค้าไม่พอ/หมดสต็อก (คงเหลือเพียง {item.stock} ชิ้น)")
            return False
            
        return True

    def add_to_cart(self, product_id: str, quantity: int) -> bool:
        #บันทึกรายการสินค้าลงตะกร้า
        if self.is_stock_available(product_id, quantity):
            product = self.products[product_id]
            subtotal = product.price * quantity

            self.cart.append({
                'product_id': product_id,
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'subtotal': subtotal
            })
            print(f"บันทึกรายการสำเร็จ: {product.name} x {quantity} ชิ้น ({subtotal:.2f} บาท)")
            return True
        return False

    def get_cart_total(self) -> float:
        #คำนวณราคารวมทั้งหมดในตะกร้า
        return sum(item['subtotal'] for item in self.cart)

    def display_cart(self):
        #แสดงรายการสินค้าทั้งหมดในตะกร้า
        print("\n---------------- รายการสินค้าในตะกร้า ----------------")
        for idx, item in enumerate(self.cart, 1):
            print(f"{idx}. {item['name']} x {item['quantity']} ชิ้น = {item['subtotal']:.2f} บาท")
        print(f"ราคารวมทั้งสิ้น: {self.get_cart_total():.2f} บาท")
        print("-----------------------------------------------------")

    def process_payment(self) -> float:
        #คำนวณราคารวม รับเงิน และคิดเงินทอนตาม Flowchart
        total = self.get_cart_total()
        print(f"\nยอดที่ต้องชำระทั้งหมด: {total:.2f} บาท")
        
        while True:
            try:
                cash = float(input("กรุณาระบุจำนวนเงินที่รับจากลูกค้า: "))
                if cash < total:
                    print(f"แจ้งเตือน: เงินไม่พอชำระ! ขาดอีก {total - cash:.2f} บาท (กรุณารับเงินใหม่)")
                else:
                    change = cash - total
                    print(f"รับเงินมา: {cash:.2f} บาท | เงินทอน: {change:.2f} บาท")
                    return change
            except ValueError:
                print("แจ้งเตือน: กรุณากรอกตัวเลขจำนวนเงินให้ถูกต้อง")

    def update_stock(self, change: float):
        #ตัดสต็อกสินค้า พิมพ์ใบเสร็จ และอัปเดตลงไฟล์
        # 1. ตัดสต็อกสินค้าในระบบ
        for item in self.cart:
            p_id = item['product_id']
            qty = item['quantity']
            self.products[p_id].stock -= qty

        # 2. พิมพ์ใบเสร็จรับเงิน
        print("\n=================== ใบเสร็จรับเงิน ===================")
        print("                 CASHIER RECEIPT                    ")
        print("-----------------------------------------------------")
        for item in self.cart:
            print(f"{item['name']:<20} x{item['quantity']:<3} {item['subtotal']:>10.2f} บาท")
        print("-----------------------------------------------------")
        print(f"ราคารวม: {self.get_cart_total():>35.2f} บาท")
        print(f"เงินทอน: {change:>36.2f} บาท")
        print("=====================================================\n")

        # 3. เซฟข้อมูลสต็อกล่าสุดกลับลงไฟล์ products.txt
        self.save_products_to_file()

        # 4. ล้างตะกร้าสินค้า
        self.cart.clear()

    def run(self):
        #ฟังก์ชันหลักระบบแคชเชียร์
        print("\nยินดีต้อนรับเข้าสู่ระบบ Cashier Program")
        
        while True:
            # ดึงข้อมูลจากไฟล์ products.txt ใหม่ทุกครั้งที่เริ่มรับลูกค้ารายใหม่
            if not self.load_products_from_file():
                break

            self.check_stock()
            
            while True:
                p_id = input("\nกรอกรหัสสินค้าที่ต้องการสั่งซื้อ (หรือกด Enter เพื่อคิดเงิน): ").strip().upper()
                
                if not p_id:
                    if not self.cart:
                        print("ยังไม่มีสินค้าในตะกร้า กรุณาเลือกสินค้าก่อนครับ")
                        continue
                    break
                
                if p_id not in self.products:
                    print("ไม่พบรหัสสินค้านี้ในระบบ กรุณาลองใหม่")
                    continue
                
                try:
                    qty = int(input(f"ระบุจำนวนสำหรับ [{self.products[p_id].name}]: "))
                    if qty <= 0:
                        print("จำนวนสินค้าต้องมากกว่า 0")
                        continue
                    self.add_to_cart(p_id, qty)
                except ValueError:
                    print("กรุณากรอกจำนวนเป็นตัวเลขจำนวนเต็มเท่านั้น")
                
                more = input("เลือกสินค้าเพิ่มอีกไหม? (y/n): ").strip().lower()
                if more != 'y':
                    break

            self.display_cart()
            change = self.process_payment()
            self.update_stock(change)
            
            next_customer = input("มีลูกค้ารายต่อไปไหม? (y/n): ").strip().lower()
            if next_customer != 'y':
                print("\nปิดการทำงานระบบแคชเชียร์ สวัสดีครับ")
                break


if __name__ == "__main__":
    app = Cashier("A2/products.txt")
    app.run()