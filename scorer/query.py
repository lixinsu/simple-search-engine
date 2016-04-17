# -*- encoding:utf-8 -*-
import pickle
import jieba

term2info = pickle.load(open(r'E:\python_project\search-engine\data\dict', 'rb'))
#uid2len = pickle.load(open(r'E:\python_project\search-engine\data\doc_length', 'rb'))
#id2news = pickle.load(open(r'E:\python_project\search-engine\data\edu-save.pickle', 'rb'))
print 'init over'

def query_parse(query_str):
    word2vect = {}
    seg_list = jieba.cut_for_search(query_str)
    for term in seg_list:
        if term in u'(),.，.。？：:；;':
               continue
        word2vect[term] = word2vect.get(term, 0) + 1
    return word2vect

def bool_query(w2d):
    docs = set([])
    k = u"查重率"
    #print "{} hits {} docs : {}".format(k,len(term2info[k]['posting'].keys()),term2info[k]['posting'].keys())
    print term2info[k]['posting'].keys()
    #docs.add(term2info[k]['posting'].keys())
    print docs

def query(w2d):
    pass

w2d = query_parse(u"中国")
bool_query(w2d)