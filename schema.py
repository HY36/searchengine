# coding=utf-8

# __author__ = 'hy'

from whoosh import fields

# JIEBA 中文分词系统
from jieba.analyse import ChineseAnalyzer

analyzer = ChineseAnalyzer()


class ContentSchema(fields.SchemaClass):
    """
    ContentSchema类是用于设置搜索引擎的 Schema

    Attributes:
    path：用于储存当前对象物理储存位置
    db_id：用于储存当前对象对应文章储存库的 ID
    anchor_id：主播ID
    anchor_name：主播名
    room_id：房间ID
    room_name：房间名
    channel：频道
    """
    path = fields.ID(unique=True, stored=True)
    object_id = fields.STORED
    object_name = fields.TEXT(stored=True, analyzer=analyzer)
    object_type = fields.STORED
