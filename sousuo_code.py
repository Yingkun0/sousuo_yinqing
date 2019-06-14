#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
python网课，第十二节案例
'''
class SearchEngineBase(object):
    def __init__(self):
        print('enter in SearchEngineBase __init__()')
        pass

    def add_corpus(self, file_path):
        with open(file_path,'r') as f:
            text = f.read()
        #print(text)
        self.process_corpus(file_path,text)


    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented.')


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        print('enter in SimpleEngine __init__()')
        super(SimpleEngine,self).__init__()
        self._id_to_texts = {}

    def process_corpus(self, id, text):
        self._id_to_texts[id] = text

    def search(self, query):
        results = []
        for id,text in self._id_to_texts.items():
            if query in text:
                results.append(id)
        return results


import re


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)  #将文档拆成set单词集合

    def search(self, query):
        query_words = self.parse_text_to_words(query)   #将输入的查询词组，拆成单词集合
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)


def main(search_engine):
    file_paths = ['1.txt','2.txt','3.txt','4.txt','5.txt']
    for file_path in file_paths:
        search_engine.add_corpus(file_path)
    while True:
        #query = input('Please input query word:')
        query = 'little'
        results = search_engine.search(query)
        length = len(results)
        if length != 0:
            print('found {} txt(s) \n{}'.format(length,results))
        else:
            print('found 0 txt')


if __name__ == '__main__':
    search_engine = SimpleEngine()
    search_engine1= BOWEngine()
    main(search_engine1)