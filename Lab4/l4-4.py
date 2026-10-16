#durian
count = 0
total_weight = 0

while True:
    weight = float(input("Please input Durian weight: "))
    if weight == 0:
        break
    count += 1
    total_weight += weight

print(f"Total of {count} Durians")
if count > 0:
    print(f"Average weight is {total_weight / count:.1f}")
else:
    print("Average weight is 0")