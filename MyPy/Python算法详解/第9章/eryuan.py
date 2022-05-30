#!/usr/bin/env python
# -*- coding:utf-8 -*-

def make_sum(a, b):
    return ['+', a, b]

def make_prod(a, b):
    return ['*', a, b]

def make_diff(a, b):
    return ['-', a, b]

def make_div(a, b):
    return ['/', a, b]

def is_basic_exp(a):
    return not isinstance(a, list)

def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex))

#表达式计算
def eval_exp(e, values):
    if is_basic_exp(e):
        #如果e位于字典里则返回键对应的值，否则直接返回e
        if e in values.keys():
            return values[e]
        else:
            return e
    op, a, b = e[0], eval_exp(e[1], values), eval_exp(e[2], values)
    if op=='+':
        return eval_sum(a, b)
    elif op=='-':
        return eval_diff(a, b)
    elif op=='*':
        return eval_prod(a, b)
    elif op=='/':
        return eval_div(a, b)
    else:
        raise ValueError("Unknown operator:", op)

#加法
def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a+b
    if is_number(a) and a==0:
        return b
    if is_number(b) and b==0:
        return a
    return make_sum(a, b)

#减法
def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    if is_number(a) and a==0:
        return -b
    if is_number(b) and b==0:
        return a
    return make_diff(a, b)

#乘法
def eval_prod(a, b):
    if is_number(a) and is_number(b):
        return a * b
    if is_number(a) and a==0:
        return 0
    if is_number(b) and b==0:
        return 0
    return make_prod(a, b)

#除法
def eval_div(a, b):
    if is_number(a) and is_number(b):
        return a / b
    if is_number(a) and a==0:
        return 0
    if is_number(b) and b==1:
        return a
    if is_number(b) and b==0:
        raise ZeroDivisionError
    return make_div(a, b)

#取出表达式里所有变量的集合
var_list = []  #这里使用全局变量
def varibles(exp):
    for i in range(1,3):
        if is_basic_exp(exp[i]):
            var_list.append(exp[i])
        else:
            varibles(exp[i])
    return var_list


if __name__=='__main__':
    e1 = make_prod(make_sum('a',3), make_sum('b',make_sum(4,6)))
    print(e1)
    print("变量集合：",varibles(e1))
    values = {}
    values['a'] = 3
    values['b'] = 4
    print(values)
    print(eval_exp(e1, values))