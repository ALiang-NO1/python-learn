#!/usr/bin/env python
# -*- coding:utf-8 -*-

class BinTreeValueError(ValueError):
    pass

class BinTreeList(object):
    def __init__(self, data, left = None, right = None):
        self.btree = [data, left, right]
    #判断二叉树是否为空
    def is_empty_bintree(self):
        return self.btree[0] is None
    #返回根节点的值
    def root(self):
        return self.btree[0]
    #返回左子树
    def left(self):
        return self.btree[1]
    #返回右子树
    def right(self):
        return self.btree[2]
    #设置根值
    def set_root(self, data):
        if data is None:
            raise BinTreeValueError("root can't be empty")
        else:
            self.btree[0] = data
    #设置左子树
    def set_left(self, left):
         if self.is_empty_bintree():
             raise BinTreeValueError("root is empty")
         elif isinstance(left, BinTreeList):
             self.btree[1] = left.btree
         else:
             self.btree[1] = left
    #设置右子树
    def set_right(self, right):
        if self.is_empty_bintree():
            raise BinTreeValueError("root is empty")
        elif isinstance(right, BinTreeList):
            self.btree[2] = right.btree
        else:
            self.btree[2] = right

if __name__ == "__main__":
    t = BinTreeList(1)
    print(t.btree)
    print(t.is_empty_bintree())
    t1 = BinTreeList(2)
    t.set_left(t1)
    print(t.btree)
    t2 = BinTreeList(3)
    t.set_right(t2)
    print(t.btree)
    t.set_root(4)
    print(t.btree)
    t4 = BinTreeList(5)
    t1.set_left(t4)
    print(t.btree)
    t1.set_right(6)
    print(t.btree)