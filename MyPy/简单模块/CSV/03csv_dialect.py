import csv

csv.register_dialect('mydialect', delimiter='●', quoting=csv.QUOTE_ALL)

with open('mydialect.csv', 'r') as myFile:
    lines = csv.reader(myFile, 'mydialect')
    print(lines.line_num)
    for line in lines:
        print(line)
csv.unregister_dialect('mydialect')