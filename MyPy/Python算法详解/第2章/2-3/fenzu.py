rows = [
    {'address': '5412 N CLARK', 'data': '07/01/2018'},
    {'address': '5232 N CLARK', 'data': '07/04/2018'},
    {'address': '5542 E 58ARK', 'data': '07/02/2018'},
    {'address': '5152 N CLARK', 'data': '07/03/2018'},
    {'address': '7412 N CLARK', 'data': '07/02/2018'},
    {'address': '6789 w CLARK', 'data': '07/03/2018'},
    {'address': '9008 N CLARK', 'data': '07/01/2018'},
    {'address': '2227 W CLARK', 'data': '07/04/2018'}
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('data'))
for data, items in groupby(rows, key=itemgetter('data')):
    print(data)
    for i in items:
        print(' ', i)
        
from collections import defaultdict

rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row['data']].append(row)

for r in rows_by_date['07/04/2018']:
    print(r)