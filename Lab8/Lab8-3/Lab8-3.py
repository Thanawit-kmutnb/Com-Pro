class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def show(self):
        for row in self.data:
            print(row)
        print()

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("ไม่สามารถบวกเมทริกซ์ได้ เนื่องจากขนาดไม่เท่ากัน")
            return None

        result = []
        i = 0
        while i < self.rows:
            row = []
            j = 0
            while j < self.cols:
                row.append(self.data[i][j] + other.data[i][j])
                j += 1
            result.append(row)
            i += 1

        return Matrix(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("ไม่สามารถลบเมทริกซ์ได้ เนื่องจากขนาดไม่เท่ากัน")
            return None

        result = []
        i = 0
        while i < self.rows:
            row = []
            j = 0
            while j < self.cols:
                row.append(self.data[i][j] - other.data[i][j])
                j += 1
            result.append(row)
            i += 1

        return Matrix(result)

    def multiplication(self, other):
        if self.cols != other.rows:
            print("ไม่สามารถคูณเมทริกซ์ได้ (จำนวนคอลัมน์ของ A ต้องเท่ากับจำนวนแถวของ B)")
            return None

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)

        return Matrix(result)



A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])

print("=== Matrix A ===")
A.show()

print("=== Matrix B ===")
B.show()

print("=== Matrix A + B (Add) ===")
C_add = A.add(B)
if C_add:
    C_add.show()

print("=== Matrix A - B (Subtract) ===")
C_sub = A.subtract(B)
if C_sub:
    C_sub.show()

print("=== Matrix A * B (Multiplication) ===")
C_mul = A.multiplication(B)
if C_mul:
    C_mul.show()