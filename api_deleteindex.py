# -*- coding:utf-8 -*-

# __author__ = 'hy'

from search import VFSearch
from flask import Flask, request, jsonify
from queue import Queue
import time,threading


app = Flask(__name__)
queue = Queue()


class DeleteIndex(threading.Thread):
    def run(self):
        global queue
        data = []
        search = VFSearch()
        while True:
            time.sleep(5)
            while queue.is_empty() == False:
                for i in range(0,queue.size()):
                    data.append(queue.get())
                num = search.delete_documents(data)
                print num

@app.route('/api/v1/search/deleteindex', methods=['POST'])
def home():

    global queue
    object_id = request.form['object_id']
    object_type = request.form['object_type']
    documents = {"object_id": object_id, "object_type": object_type}
    queue.put(documents)
    return jsonify({'OK': '200'})


if __name__ == "__main__":
    delete = DeleteIndex()
    delete.start()
    app.run(host='0.0.0.0', port=19997, debug=True, threaded=True)
