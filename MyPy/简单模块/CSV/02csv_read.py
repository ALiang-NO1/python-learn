import csv

with open('test.csv', 'r') as f:
    lines = csv.reader(f)
    print(lines.dialect.delimiter)
    for line in lines:
        print("第%s行:" % lines.line_num, line)