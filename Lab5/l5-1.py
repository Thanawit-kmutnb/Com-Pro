#find min/max/average
def find_max(numbers):
    max_val = numbers[0]
    for i in numbers:
        if i > max_val:
            max_val = i
    return max_val

def find_min(numbers):
    min_val = numbers[0]
    for i in numbers:
        if i < min_val:
            min_val = i
    return min_val

def find_avg(numbers):
    sum = 0
    count = 0
    for i  in numbers:
        sum += i
        count += 1
    result = sum / count

    return result

def find_max_index(numbers):
    max_idx = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_idx]:
            max_idx = i
    return max_idx

def find_min_index(numbers):
    min_idx = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_idx]:
            min_idx = i
    return min_idx

def find_value(numbers,target):
    for i in range(0,len(numbers)):
        if numbers[i] == target:
            return i
    return -1

def count_higher_than_average(numbers):
    avg = find_avg(numbers)
    count = 0
    for i in range(0,len(numbers)):
        if numbers[i] > avg:
            count = count + 1

    return count

def is_increasing(numbers):
    for i in range(0, (len(numbers)-1)):
        if numbers[i] > numbers[i+1]:
            return False

    return True

#print(find_max([60,30,55]))
#print(find_min([60,30,55]))
#print(find_avg([60,30,30]))
#print(find_max_index([60,50,80]))
#print(find_min_index([60,50,80]))
#print(find_value([60,30,45,55],60))
#print(count_higher_than_average([60,50,70,65]))
print(is_increasing([40,45,60,55]))