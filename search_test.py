# -*- coding:utf-8 -*-
import requests, json

# 更新索引
# url = "http://127.0.0.1:19998/api/v1/searchengine/updateindex"
# data = {}
# data['anchor_id'] = raw_input('请输入主播ID：')
# data['anchor_name'] = raw_input('请输入主播名字：')
# data['room_id'] = raw_input('请输入直播间ID：')
# data['room_name'] = raw_input('请输入直播间名称：')
# data['channel'] = raw_input('请输入频道名：')
# end = requests.post(url, data)
# print end.text

# 添加索引
# url = "http://127.0.0.1:19996/api/v1/searchengine/addindex"
# data = {}
# data['object_id'] = 56
# data['object_name'] = "xbox英雄"
# data['object_type'] = "anchor"
# end = requests.post(url, data)
# print end

# 删除索引
url = "http://127.0.0.1:19997/api/v1/search/deleteindex"
data = {}
data['object_id'] = 56
data['object_type'] = "anchor"
end = requests.post(url, data)
print end.content
# 搜索
# url = "http://10.20.22.17:8077/api/v1/search/?key=%E8%8B%B1%E9%9B%84"
# # data = {}
# # data['key'] = raw_input('请输入主播名/房间名/频道：')
# end = requests.get(url)
# print end.text

# end = requests.post(url, data = {'key':u'马云'})
# print end.text