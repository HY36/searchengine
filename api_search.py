# -*- coding:utf-8 -*-

# __author__ = 'hy'


from search import VFSearch
from flask import Flask, jsonify, request


app = Flask(__name__)
@app.route('/api/v1/searchengine/search', methods=['POST'])
def home():

    search = VFSearch()
    search_key = request.form['key']
    result = search.search_in_key(search_key)
    return jsonify(result)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=19995, debug=True, threaded=True)
