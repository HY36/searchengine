# -*- coding:utf-8 -*-

# Project: search
# File name: config
# Creator: hy
# Date: 6/29/16 - 10:06 AM

# authorship
__author__ = 'hy'
__status__ = 'Development'

from pymongo import MongoClient
from search import VFSearch
import requests


class createindex():
    client = None
    cms_index = None

    def setUp(self):
        self.client = MongoClient('10.20.22.131', 27017)

    def creat_index(self):
        db = self.client.news

        articles = db.article.find({"article_source":"央视"})
        self.cms_search = VFSearch()
        article_list = []

        for index, article in enumerate(articles):
            if 'article_content' not in article:
                continue
            if 'article_title' not in article:
                continue
            article_list.append({
                'title': unicode(
                    article['article_title'].encode("unicode_escape")),
                'content': unicode(
                    article['article_content'].encode("unicode_escape")),
                'keywords': unicode(article['article_abstract'].encode(
                    "unicode_escape")),
                'db_id': unicode(str(article['_id']).encode("unicode_escape")),
                'article_type': 1
            })

        self.client.close()

        # self.cms_search.add_document_archor(article_list)
def main():

    url = "http://127.0.0.1:19995/api/v1/searchengine/search"
    data = {}
    data['key'] = raw_input('请输入主播名/房间名/频道：')
    end = requests.post(url, data)
    print end.text
if __name__ == '__main__':
    main()