import csv

with open('test.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([2, 'b'])
    writer.writerow(['g', 'c'])
    li = [[1, 2, 3], ['aa', 'bb', 'cc']]
    writer.writerows(li)