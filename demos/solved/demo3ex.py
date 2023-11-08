def max_number(numbers: list[int]) -> int | None:
    result = None
    for number in numbers:
        if result is None or number > result:
            result = number
    return result


test1: int | None = max_number([1, 2, 3, 5, 4])
print(test1)
assert isinstance(test1, int)
print('max is greater than 42?', test1 > 42)

test2: int | None = max_number([])
print(test2)
if isinstance(test2, int):
    print('max is greater than 42?', test2 > 42)
else:
    print('no result')
