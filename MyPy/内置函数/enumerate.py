sequence = ('aa', 'bbbb', 'ccccc', 'ddd')
a = enumerate(sequence)
print(a)
print(list(a))

b = enumerate(sequence, 4)
print(list(b))
