def max_number(numbers):
    result = None
    for number in numbers:
        if result is None or number > result:
            result = number
    return result


test1 = max_number([1, 2, 3, 5, 4])
print(test1)
print('max is greater than 42?', test1 > 42)

test2 = max_number([])
print(test2)
print('max is greater than 42?', test2 > 42)
