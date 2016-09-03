# -*- coding:utf-8 -*-

# __author__ = 'hy'

from search import VFSearch
from flask import Flask, jsonify, request
import threading
import Queue
import time

app = Flask(__name__)

queue = Queue.Queue(maxsize=0)
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)


class UpdateIndex(threading.Thread):
    def run(self):
        data = []
        global queue
        search = VFSearch()
        while True:
            time.sleep(5)
            while queue.empty() == False:
                for i in range(0,queue.qsize()):
                    data.append(queue.get())
                search.update_documents(data)
                for i in range(len(data)-1, -1, -1):
                    data.pop(i)

@app.route('/api/v1/searchengine/updateindex',methods=['POST'])
def update_item():
    global queue
    object_id = request.form['object_id']
    object_name = request.form['object_name']
    object_type = request.form['object_type']
    documents = {"object_id":object_id, "object_name":object_name, "object_type":object_type}
    queue.put(documents)
    return  jsonify({'OK': '200'})



    # for i in range(len(result)):
    #     data[i] = result[i]['anchor_name']

    # return jsonify(result)


if __name__ == "__main__":
    update = UpdateIndex()
    update.start()
    app.run(host='0.0.0.0', port=19998, debug=True, threaded=True)

    # while True:
    #     time.sleep(60)



