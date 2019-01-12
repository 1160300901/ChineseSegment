#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: sunyueqing
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: sunyueqinghit@163.com
@File : segment.py
@Time : 2018/12/4 16:22
@Site : 
@Software: PyCharm
'''

import re


def extract(rawfile, resultfile):
    '''
    提取分词标准文件，作为计算准确率的参照
    :param rawfile: 2004_corpus.txt,2004年人民日报带词性标注的语料
    :param resultfile: 2004_seg.txt,从预料库删去词性，得到分词标准文件
    :return:
    '''
    f_raw = open(rawfile, "r", encoding="GB18030")
    f_result = open(resultfile, "w", encoding="GB18030")

    for line in f_raw.readlines():
        if len(line.strip()) == 0:
            continue
        line = re.sub("[/a-zA-Z]+", "/", line)
        line = re.sub("/1", "/", line)
        line = re.sub("（）", "", line)
        line = re.sub("]/", "", line)
        line = re.sub("\[", "", line)
        line = re.sub("（/ / ）/ ", "", line)
        line = line.replace("1", "１")
        line = line.replace("2", "２")
        line = line.replace("3", "３")
        line = line.replace("4", "４")
        line = line.replace("5", "５")
        line = line.replace("6", "６")
        line = line.replace("7", "７")
        line = line.replace("8", "８")
        line = line.replace("9", "９")
        line = line.replace("0", "０")
        line = line.replace("%", "％")

        f_result.write(line)
    f_result.close()
    f_raw.close()


def main():
    extract("2004_corpus.txt", "seg.txt")


if __name__ == '__main__':
    main()
