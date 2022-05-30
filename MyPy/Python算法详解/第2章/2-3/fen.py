from itertools import groupby
from operator import itemgetter
things = [('2018-05-21', 11), ('2018-05-21', 3), ('2018-05-22', 10),
          ('2018-05-22', 4), ('2018-05-22', 22),('2018-05-23', 33)]
for key, items in groupby(things, itemgetter(0)):
   print(key)

for subitem in items:
  print(subitem)
print('-' * 20)