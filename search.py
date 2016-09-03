# -*- coding:utf-8 -*-

# __author__ = 'hy'


import os

from whoosh.qparser import MultifieldParser
from whoosh import index


from config import WHOOSH_CONFIG
from schema import ContentSchema


index_dir = "F:/searchengine/index"

class UnicodeTypeException(Exception):
    pass


class VFSearch:
    ix = None
    writer_config = {}

    def __init__(self):
        if not os.path.exists(index_dir):
            os.mkdir(index_dir)

        if index.exists_in(index_dir):
            self.ix = index.open_dir(index_dir)
        else:
            self.ix = index.create_in(index_dir, ContentSchema)


    @staticmethod
    def get_index(storage):
        """
        获取 index
        :return: indexObject
        """
        return storage.open_index()

    @staticmethod
    def create_index(storage):
        return storage.create_index(ContentSchema)

    def close_index(self):
        return self.ix.close()

    def config_writer(self):
        self.writer_config = {
            'limitmb': WHOOSH_CONFIG['WHOOSH_RAM_LIMIT'],
            'procs': WHOOSH_CONFIG['WHOOSH_PROCESSOR_LIMIT'],
            'multisegment': WHOOSH_CONFIG['WHOOSH_MULTI_SEGMENT']
        }

    def validate_text(self, text):
        if not isinstance(text, unicode):
            raise UnicodeTypeException("input should be unicode")

    def validate_texts(self, *args):
        for text in args:
            self.validate_text(text)

    def add_document(self, object_id, object_name, object_type):
        self.validate_texts(object_name)
        with self.ix.writer(**self.writer_config) as writer:
            path = '%s/%s' % (object_id, object_name)
            writer.add_document(path=path,
                                object_name=object_name,
                                object_type=object_type,
                                object_id=object_id)

    def add_documents(self, documents):
        # 批量添加索引
        with self.ix.writer(**self.writer_config) as writer:
            for document in documents:
                object_id = document['object_id']
                object_name = document['object_name']
                object_type = document['object_type']
                self.validate_texts(object_name)
                path = '%s/%s' % (object_id, object_type)
                writer.add_document(path=path,
                                    object_name=object_name,
                                    object_type=object_type,
                                    object_id=object_id)


    def update_documents(self, documents):
        # 批量更新索引
        with self.ix.writer(**self.writer_config) as writer:
            for document in documents:
                object_id = document['object_id']
                object_name = document['object_name']
                object_type = document['object_type']
                self.validate_texts(object_name)
                path = '%s/%s' % (object_id, object_type)
                writer.add_document(path=path,
                                    object_name=object_name,
                                    object_type=object_type,
                                    object_id=object_id)



    def delete_documents(self, documents):
        #批量删除索引
        with self.ix.writer(**self.writer_config) as writer:
            fieldname = 'path'
            for index, document in enumerate(documents):
                object_id = document['object_id']
                object_type = document['object_type']
                path = '%s/%s' % (object_id, object_type)
                writer.delete_by_term(fieldname, path)



    # def search_in_key(self, key):
    #     # 搜索
    #     ix = self.ix
    #
    #     with ix.searcher() as searcher:
    #         query = MultifieldParser(["anchor_name","room_name","channel"], schema=ix.schema)
    #         user_query = query.parse(key)
    #         results = searcher.search(user_query, limit=None)
    #
    #         search_value = [{'anchor_id':result['anchor_id'],
    #                          'room_id':result['room_id'],
    #                          'anchor_name': result['anchor_name'],  # decode("unicode_escape")
    #                          'room_name':result['room_name'],
    #                          'channel': result['channel']
    #                          } for result in results]
    #
    #     return search_value

    def search_in_key(self, key):
        # 搜索
        ix = self.ix

        with ix.searcher() as searcher:
            query = MultifieldParser(['object_name'], schema=ix.schema)
            user_query = query.parse(key)
            results = searcher.search(user_query, limit=None)

            search_value = [{'id': result['object_id'],
                             'name': result['object_name'],  # decode("unicode_escape")
                             'type': result['object_type'],
                             'path':result['path']
                             } for result in results]
            print search_value

        return search_value

    def search_in_type(self, key, page_number):
        # 分页搜索
        ix = self.ix

        with ix.searcher() as searcher:
            query = MultifieldParser(["anchor_name", "room_name", "channel"], schema=ix.schema)
            user_query = query.parse(key)
            results = searcher.search_page(user_query, page_number, pagelen=10)

            search_value = [{'anchor_id': result['anchor_id'],
                             'room_id': result['room_id'],
                             'anchor_name': result['anchor_name'],  # decode("unicode_escape")
                             'room_name': result['room_name'],
                             'channel': result['channel']
                             } for result in results]
            return search_value
