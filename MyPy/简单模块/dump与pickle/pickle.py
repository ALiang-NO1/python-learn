import pickle
import time

entry = {}
entry['title'] = 'Dive into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive‐intohistory‐2009‐edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')

with open('entry.pickle', 'wb') as f:
    pickle.dump(entry, f)
with open('entry.pickle', 'rb') as f:
    entry2 = pickle.load(f)
    print('entry2:', entry2)
    print('tags:', entry2['tags'])
    print('entry==entry2:', entry == entry2)