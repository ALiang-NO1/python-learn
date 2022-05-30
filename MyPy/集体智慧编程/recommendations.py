critics = {
    'Lisa Rose': {
        'Lady in Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
        'The Night Listener': 3.0
    },
    'Michael Phillips': {
        'Lady in Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 4.5
    },
    'Mick LaSalle': {
        'Lady in Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'You, Me and Dupree': 2.0,
        'The Night Listener': 3.0
    },
    'Jack Matthews': {
        'Lady in Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
        'The Night Listener': 3.0
    },
    'Toby': {
        'Snakes on a Plane': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 1.0
    }}

# 欧几里得距离评价：通过二维坐标上点的距离估计偏好相似度
from math import sqrt

def sim_distance(prefs, person1, person2):
    """返回有关 person1 person2 基于距离的相似度评价"""
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    sun_of_square = sum([pow(prefs[person1][item]-prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sqrt(sun_of_square))

# sim = sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
# print(sim)

# 皮尔逊相关度评价：判断两种数据与一条直线拟合度，用于数据不是很规范时，修正“夸大分值”
def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    n = len(si)
    if n == 0:
        return 1
    # 对所有共同偏好求和
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # 求平方和
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # 求乘积和
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
    # 计算皮尔逊评价值
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2, 2)/n))
    if den == 0:
        return 0
    return num/den  # 返回值：-1~1（1：完全一致）
# print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[:n]
top = topMatches(critics, 'Toby', n=3)
print(top)
