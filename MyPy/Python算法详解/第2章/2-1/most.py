words = [
'look', 'into', 'my', 'AAA', 'look', 'into', 'my', 'AAA',
'the', 'AAA', 'the', 'AAA', 'the', 'eyes', 'not', 'BBB', 'the',
'AAA', "don't", 'BBB', 'around', 'the', 'AAA', 'look', 'into',
'BBB', 'AAA', "BBB", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
