# -*- encoding:utf-8 -*-
import codecs
import jieba
import json
import os
import pickle
from model.news import news
import time
"""
简单的基于内存的搜索引擎
"""


def filter_encode(path, newsfile):
    """
    把新闻过滤一下
    :param path:
    :param newsfile:
    :return:
    """
    infile = os.path.join(path,newsfile)
    id2news  =  {}
    with codecs.open(infile, 'r', 'utf-8') as infp:
        for line in infp:
            row = line.strip().split('\t')
            if len(row) < 6:
                continue
            try:
                news_date = row[2].split(u'来源:')[0].strip()
                news_src = row[2].split(u'来源:')[1].strip()
            except IndexError:
                news_date = row[2].strip()
                news_src = ""
                # print row[2]
            thenews = news(row[1], news_date, news_src, row[3], row[4], row[5])
            id2news[row[0]] = thenews.tostr()
        print 'doc num',len(id2news)
        pickle.dump( id2news, open(os.path.join(path,newsfile.replace('.txt','')+"-save.pickle"), "wb" ))

def cn_tokenizer(path, picklefile):
    """
    读取pickle文件，分词建立建立词表并将文档向量化
    :param path:
    :param newsfile:
    :return:
    """
    print 'start indexer'
    print 'indexing.....'
    s_time = time.time()
    term2info = {}
    uid2len = {}
    infile = os.path.join(path, picklefile)
    id2news = pickle.load( open( infile, "rb" ) )
    # 遍历所有文档
    cnt =0
    for k ,v in id2news.items():
        cnt +=1
        print cnt
        uid = k
        v = json.loads(v)
        news = v['title'] * 3 + v['text']
        seg_list = jieba.cut_for_search(news)
        # process each doc
        doc_len = 0
        # 遍历词条
        for term in seg_list:
            if term in u'(),.，.。？：:；;':
                continue
            doc_len += 1
            if term not in term2info:
                term2info[term] = {}
                term2info[term]['total_freq'] = 0
                term2info[term]['posting'] = {}
                term2info[term]['posting'][uid] = 0
                term2info[term]['docs'] = 0
            term2info[term]['total_freq'] += 1
            if uid not in term2info[term]['posting'].keys():
                term2info[term]['posting'][uid] = 0
            term2info[term]['posting'][uid] += 1
            term2info[term]['docs'] = len(term2info[term]['posting'])
        # 记录文档长度
        uid2len[uid] = doc_len    
        #print json.dumps(term2info)
        #print json.dumps(uid2len)
    pickle.dump(term2info, open(os.path.join(path,"dict"), "wb" ))
    pickle.dump(uid2len, open(os.path.join(path,"doc_length"), "wb" ))
    e_time = time.time()
    print 'index succeed'
    print "time used :{}".format(e_time-s_time)

if __name__ == "__main__":
    filename = 'edu.txt'
    # filter_encode(r'E:\python_project\search-engine\data', 'edu.txt')
    cn_tokenizer(r'E:\python_project\search-engine\data', filename.replace('.txt','')+"-save.pickle")
