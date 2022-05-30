from operator import itemgetter
rows = [
    {'fname': 'AAA', 'lname': 'ZHANG', 'uid': 1001},
    {'fname': 'BBB', 'lname': 'ZHOU', 'uid': 1002},
    {'fname': 'CCC', 'lname': 'WU', 'uid': 1004},
    {'fname': 'DDD', 'lname': 'LI', 'uid': 1003}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['fname'], r['lname']))
print(rows_by_fname)
print(rows_by_lfname)
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))