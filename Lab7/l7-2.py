my_array = [
    [10, 20, 55],
    [30, 40, 50],
    [5, 15, 25]
]

def find_max(arr):
    max_val = arr[0][0]
    for row in arr:
        for val in row:
            if val > max_val:
                max_val = val
    return max_val

def find_min(arr):
    min_val = arr[0][0]
    for row in arr:
        for val in row:
            if val < min_val:
                min_val = val
    return min_val

def find_average(arr):
    return sum(val for row in arr for val in row) / sum(len(row) for row in arr)

#---------------------------------------------------
def is_found(arr, target):
    for row in arr:
        for val in row:
            if val == target:
                return True
    return False

#---------------------------------------------------
def matrix_add(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result

def matrix_subtract(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] - B[i][j]
    return result

def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Max:", find_max(my_array))
print("Min:", find_min(my_array))
print("Avg:", find_average(my_array))
print("Found 55:", is_found(my_array, 55))
print("Found 99:", is_found(my_array, 99))
print("Add:", matrix_add(A, B))
print("Sub:", matrix_subtract(A, B))
print("Mul:", matrix_multiply(A, B))