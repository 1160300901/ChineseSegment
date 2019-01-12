#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: sunyueqing
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: sunyueqinghit@163.com
@File : sentence.py
@Time : 2018/12/4 16:12
@Site : 
@Software: PyCharm
'''

import re


def extract(rawfile, resultfile):
    '''
    生成用于分词的生文本
    :param rawfile: 2004_seg.txt,分词标准文件
    :param resultfile: 2004_sentence.txt,去除分词，得到即将分词的句子
    :return:
    '''
    f_raw = open(rawfile, "r", encoding="GB18030")
    f_result = open(resultfile, "w", encoding="GB18030")

    for line in f_raw.readlines():
        line = re.sub("/ ", "", line)
        f_result.write(line)
    f_result.close()
    f_raw.close()


def main():
    extract("2004_seg.txt", "2004_sentence.txt")


if __name__ == '__main__':
    main()
