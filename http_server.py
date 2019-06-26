# -*- coding: utf-8 -*-


import gensim
import os
import jieba
import json
from flask import request, Flask
import argparse

app = Flask(__name__)


HERE = os.path.dirname(os.path.abspath(__file__))
BAIKE_VEC_PATH = os.path.join(HERE, 'data', 'sgns.target.word-word.dynwin5.thr10.neg5.dim300.iter5')
WORD_VEC = gensim.models.KeyedVectors.load_word2vec_format(BAIKE_VEC_PATH, binary=False)


@app.route('/similar', methods=['POST'])
def similar():
    data = json.loads(request.data())
    try:
        simi = WORD_VEC.most_similar(data['query'])
        return json.dumps(simi, ensure_ascii=False)
    except:
        return '{} not in dic'.format(data)


@app.route('/wmd', methods=['POST'])
def wmd():
    data = json.loads(request.data())
    text1 = jieba.lcut(data['text1'])
    text2 = jieba.lcut(data['text2'])
    distance = WORD_VEC.wmdistance(text1, text2)
    return json.dumps({'distance': distance}, ensure_ascii=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--host', default='0.0.0.0', help='host')
    args.add_argument('--port', default=9004, help='port')

    args = args.parse_args()

    host = args.host
    port = args.port

    app.run(host=host, port=port)



