def remove_duplicates(numbers):
    unique_num = []
    i = 0

    while i < len(numbers):
        item = numbers[i]
        if item not in unique_num:
            unique_num.append(item)
        i += 1

    return unique_num

data = [1, 2, 2, 3, 4, 4, 4, 5]
print(remove_duplicates(data))