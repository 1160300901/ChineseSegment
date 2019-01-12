#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: sunyueqing
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: sunyueqinghit@163.com
@File : binarySearchSegment.py
@Time : 2018/12/2 15:44
@Site : 
@Software: PyCharm
'''

'''
使用二分查找对分词系统速度优化
运行时间在5-6分钟波动,有误差

'''

import time


def binary_search(find, list1):
    '''
    二分查找
    :param find: 要查找的词
    :param list1: 词典列表
    :return: 如果找到返回词的下标，否则返回-1
    '''
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = (low + high) // 2
        if list1[mid] == find:
            return mid
        # 左半边
        elif list1[mid] > find:
            high = mid - 1
        # 右半边
        else:
            low = mid + 1
    # 未找到返回-1
    return -1


def add_dict(dictfile):
    """
    读入词典
    :param dictfile: 词典文件
    :return: dictionary词典列表，max_length词条的最大长度
    """
    f_dict = open(dictfile, "r+", encoding="GB18030")
    print("开始读入词典: ")
    max_length = 1
    count = 0
    dictionary = []
    for line in f_dict.readlines():
        line = line.strip()
        dictionary.append(line)
        count += 1
        if len(line) > max_length:
            max_length = len(line)
    print("    完成词典初始化，词典条目数：" + str(count))
    print("    最大分词长度：" + str(max_length))
    return dictionary, max_length


def FMM_segment(rawfile, resultfile, dictionary, max_length):
    """
    正向最大匹配
    :param rawfile: 要分词的文件
    :param resultfile: 分词后写入的文件
    :param dictionary: 词典
    :param max_length: 词典中词条的最大长度
    """
    f_raw = open(rawfile, "r", encoding="GB18030")
    f_result = open(resultfile, "w", encoding="GB18030")

    for line in f_raw.readlines():
        while len(line) > 0:
            max_len = max_length
            if len(line) < max_len:
                max_len = len(line)

            # 取指定的最大长度的文本去词典里面匹配
            try_word = line[0:max_len]
            while binary_search(try_word, dictionary) == -1:
                if len(try_word) == 1:
                    break
                try_word = try_word[0:(len(try_word) - 1)]
            if try_word is "\n":
                f_result.write(try_word)
            else:
                f_result.write(try_word + "/ ")
            line = line[len(try_word):]
    f_raw.close()
    f_result.close()


def BMM_segment(rawfile, resultfile, dictionary, max_length):
    """
    逆向最大匹配
    :param rawfile: 要分词的文件
    :param resultfile: 分词后写入的文件
    :param dictionary: 词典
    :param max_length: 词典中词条的最大长度
    """
    f_raw = open(rawfile, "r", encoding="GB18030")
    f_result = open(resultfile, "w", encoding="GB18030")

    for line in f_raw.readlines():
        result = []
        while len(line) > 0:
            max_len = max_length
            if (len(line) < max_len):
                max_len = len(line)

            try_word = line[(len(line) - max_len):]
            while binary_search(try_word, dictionary) == -1:
                if (len(try_word) == 1):
                    break
                try_word = try_word[1:]
            result.insert(0, try_word)
            # 从待分词文本中取出已经分词的文本
            line = line[0:(len(line) - len(try_word))]
        for word in result:
            if word is "\n":
                f_result.write(word)
            else:
                f_result.write(word + "/ ")
    f_raw.close()
    f_result.close()


def main():
    # 训练集
    # dictionary, max_length = add_dict("train_data/sort_dic.txt")
    # print("正在计时...\n")
    # t0 = time.time()
    # FMM_segment("train_data/199801_sent.txt", "train_data/seg_FMM.txt", dictionary, max_length)
    # BMM_segment("train_data/199801_sent.txt", "train_data/seg_BMM.txt", dictionary, max_length)
    # print("总耗时: ", time.time() - t0, " 秒")

    # 测试集
    dictionary, max_length = add_dict("train_data/sort_dic.txt")
    print("正在计时...\n")
    t0 = time.time()
    FMM_segment("test_data/sentence.txt", "test_data/seg_FMM.txt", dictionary, max_length)
    BMM_segment("test_data/sentence.txt", "test_data/seg_BMM.txt", dictionary, max_length)
    print("总耗时: ", time.time() - t0, " 秒")

if __name__ == '__main__':
    main()
