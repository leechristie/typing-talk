from collections import Counter


def most_common(items):
    if not items:
        raise ValueError('no items')
    counter = Counter(items)
    item, count = counter.most_common(1)[0]
    return item, count


i, c = most_common(['foo', 'bar', 'foo', 'baz'])
print(f"most common: '{i}' with count {c}")

i, c = most_common(['z', 'x', 'y', 'x', 'x'])
print(f"most common: '{i}' with count {c}")

i, c = most_common('one item')
print(f"most common: '{i}' with count {c}")
