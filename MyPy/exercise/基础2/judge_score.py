def fun(score):
    degree = 'DCBA'
    if score > 100 or score < 0:
        print('分数错误，分数值必须介于0—100之间')
    else:
        if score < 60:
            return'E'
        else:
            index = (score - 60)//10
            return degree[index]
