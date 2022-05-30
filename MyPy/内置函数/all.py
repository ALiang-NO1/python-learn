def test_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(test_all(['a', 'b', '']))
print(test_all(['a', 'b']))