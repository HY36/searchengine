# -*- coding:utf-8 -*-

# __author__ = 'hy'

class Queue:

    def __init__(self):
        self.items = []

    def put(self, item):
        # 放入数据
        self.items.append(item)

    def get(self):
        # 取出数据
        return self.items.pop(0)

    def is_empty(self):
        # 判断队列是否为空
        return self.size() == 0

    def size(self):
        # 返回队列大小
        return len(self.items)