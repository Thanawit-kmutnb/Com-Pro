temp_data = [
    [30, 31, 29, 32, 30, 28, 31],  # สัปดาห์ที่ 1 (w = 0)
    [33, 34, 35, 32, 31, 30, 29],  # สัปดาห์ที่ 2 (w = 1)
    [27, 28, 26, 25, 29, 28, 30],  # สัปดาห์ที่ 3 (w = 2)
    [31, 32, 33, 30, 29, 31, 32],  # สัปดาห์ที่ 4 (w = 3)
]

def week_average(data, w):
    return sum(data[w]) / len(data[w])

def week_max(data, w):
    return max(data[w])

def week_min(data, w):
    return min(data[w])

def overall_max(data):
    max_values = [week_max(data, w) for w in range(len(data))]
    return max(max_values)

def overall_min(data):
    min_values = [week_min(data, w) for w in range(len(data))]
    return min(min_values)

print("เฉลี่ยสัปดาห์แรก :", week_average(temp_data, 0))
print("สูงสุดสัปดาห์สอง :", week_max(temp_data, 1))
print("ต่ำสุดสัปดาห์สาม :", week_min(temp_data, 2))
print("---")
print("อุณหภูมิสูงสุดทั้งหมด:", overall_max(temp_data))
print("อุณหภูมิต่ำสุดทั้งหมด:", overall_min(temp_data))