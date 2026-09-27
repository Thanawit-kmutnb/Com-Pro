class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def show(self):
        print(f"Product Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

def show_max_value_product(products):
    if not products:
        print("ไม่มีข้อมูลสินค้าในระบบ")
        return

    max_product = max(products, key=lambda p: p.price * p.quantity)
    
    print("=== สินค้าที่มีมูลค่ารวมมากที่สุด ===")
    max_product.show()


products_list = []


with open("Lab8/Lab8-2/products.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                name, price, quantity = line.split(",")

                product_obj = Product(name, price, quantity)
                products_list.append(product_obj)

show_max_value_product(products_list)
