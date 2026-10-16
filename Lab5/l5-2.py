#variance
def find_variance(numbers):
    sum = 0
    count = 0
    for x in numbers:
        sum += x
        count += 1

    avg = sum / count

    result = 0
    for x in numbers:
        diff = (x - avg) ** 2
        result += diff

    variance = result/count

    return variance
