records = [
    ('AAA', 1, 2),
    ('BBB', 'hello'),
    ('CCC', 5, 3)
]


def do_foo(x, y):
    print('AAA', x, y)

def do_bar(s):
    print('BBB', s)

for tag, *args in records:
    if tag == 'AAA':
        do_foo(*args)
    elif tag == 'BBB':
        do_bar(*args)

line = 'guan:ijing234://wef:678d:guan'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)