class Vehicle():
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def show_info(self):
        print(f"License Plate: {self.license_plate}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Daily Rate: {self.daily_rate} Baht")

    def calculate_rental_cost(self, days):
        return self.daily_rate * days

class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = seats

    def show_info(self):
        super().show_info()
        print(f"Number of Seats: {self.seats}")

    def calculate_rental_cost(self, days):
        payable_days = (days // 7) * 5 + (days % 7)
        return self.daily_rate * payable_days

class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload

    def show_info(self):
        super().show_info()
        print(f"Payload Capacity: {self.payload} kg")

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)

print("=== ข้อมูลรถยนต์นั่ง (Car) ===")
my_car = Car("กข 1234", "Toyota", "Camry", 2023, 1500.0, 5)
my_car.show_info()
    
    # ทดสอบคำนวณค่าเช่า Car 7 วัน (ต้องคิดราคาเพียง 5 วัน)
days_car = 7
cost_car = my_car.calculate_rental_cost(days_car)
print(f"ค่าเช่า {days_car} วัน (โปรโมชั่น เช่า 5 แถม 2): {cost_car:,.2f} บาท")

print("\n" + "="*30 + "\n")

print("=== ข้อมูลรถบรรทุก (Truck) ===")
my_truck = Truck("ฮฮ 9999", "Isuzu", "ELF", 2022, 2500.0, 3.5)
my_truck.show_info()
    
    # ทดสอบคำนวณค่าเช่า Truck 7 วัน (คิดราคาเต็ม 7 วัน)
days_truck = 7
cost_truck = my_truck.calculate_rental_cost(days_truck)
print(f"ค่าเช่า {days_truck} วัน (ไม่มีโปรโมชั่น): {cost_truck:,.2f} บาท")