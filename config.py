# -*- coding:utf-8 -*-

# __author__ = 'hy'


WHOOSH_CONFIG = {
    'WHOOSH_RAM_LIMIT': 512, # WHOOSH 每核心内存数量
    'WHOOSH_PROCESSOR_LIMIT': 4, # WHOOSH 使用核心数
    'WHOOSH_MULTI_SEGMENT': False # 是否分段储存文件
}