def test_any(iterable):
    for element in iterable:
        if element:
            return True
    return False

print(test_any(['']))
print(test_any(['a', '']))