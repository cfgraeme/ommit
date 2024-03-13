def average(numbers):
    return sum(numbers) / len(numbers)


def mode(numbers):
    return max(set(numbers), key=numbers.count)
