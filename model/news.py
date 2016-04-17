# -*- encoding:utf-8 -*-
import json


class news(object):
    def __init__(self, url, news_date, news_src, title, hotness, text):
        self.url = url
        self.news_date = news_date
        self.news_src = news_src
        self.title = title
        self.hotness = hotness
        self.text = unicode(text)

    def disp(self):
        print "{}-{}".format(self.title,self.news_date)
        print "{}".format(self.news_src)
        i = 0
        while i < len(self.text):
            print self.text[i:i+20]
            i += 20

    def tostr(self):
        total = {}
        total['title'] = self.title
        total['date'] = self.news_date
        total['src'] = self.news_src
        total['text'] = self.text
        return json.dumps(total)



if __name__ == "__main__":
    n = news('ucas', 'sulixn', '20160203', u'国科大你好，hello,国科大你好，hello国科大你好，hello国科大你好，hello国科大你好，hello')
    n.disp()
    n.tostr()

