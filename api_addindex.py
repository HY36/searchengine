# -*- coding:utf-8 -*-

# __author__ = 'hy'

from search import VFSearch
from flask import Flask, jsonify, request
import Queue
import time, threading


app = Flask(__name__)
queue = Queue.Queue(maxsize=0)



class AddIndex(threading.Thread):
    def run(self):
        data = []
        global queue
        search = VFSearch()
        while True:
            time.sleep(5)
            while queue.empty() == False:
                for i in range(0,queue.qsize()):
                    data.append(queue.get())
                search.add_documents(data)
                for i in range(len(data)-1, -1, -1):
                    data.pop(i)


@app.route('/api/v1/searchengine/addindex', methods=['POST'])
def home():

    global queue
    object_id = request.form['object_id']
    object_name = request.form['object_name']
    object_type = request.form['object_type']
    documents = {"object_id":object_id, "object_name":object_name, "object_type":object_type}
    # search = VFSearch()
    # search.add_document(object_id=object_id, object_name=object_name, object_type=object_type)
    queue.put(documents)
    return jsonify(documents)




if __name__ == "__main__":
    add = AddIndex()
    add.start()
    app.run(host='0.0.0.0', port=19996, debug=True, threaded=True)
