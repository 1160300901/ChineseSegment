#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: sunyueqing
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: sunyueqinghit@163.com
@File : Extract_dictionary.py
@Time : 2018/12/2 10:12
@Site : 
@Software: PyCharm
'''

import re


def rm_punctuation(file, rmfile):
    punc = "。，、“”,’？！（）＋－×……《"
    f1 = open(file, "r", encoding='GB18030')
    f2 = open(rmfile, "w", encoding='GB18030')
    for line in f1.readlines():
        line_rmpunc = re.sub("[%s]+" % punc, "", line)
        f2.write(line_rmpunc)
    f1.close()
    f2.close()


def handle_dictfile(rawfile, resultfile):
    f_raw = open(rawfile, "r", encoding="GB18030")
    f_result = open(resultfile, "w", encoding="GB18030")

    dictionary = set()
    for line in f_raw.readlines():
        line = line.replace("  ", " ")
        line = line.strip().split(" ")
        for i in line:
            dictionary.add(i)

    for word in dictionary:
        word = re.sub("[/a-zA-Z]+", "", word)  # 提取不带词性的词典
        if re.match("(\d+)-(\d+)-(\d+)-(\d+)", word):  # 删去无用标签
            continue
        # if re.match("(\d+)", word):  # 删去数字
        #     continue
        # p = re.compile(r"[〈〉±％／ＭＩＣＲＯＮＡＳＤＥＹｏｕａｒｅｗｌｃｍＴ—Ｋ·ＦｄｈＵｎｉｖｓｔｙ．ｐＪＢｇＰＨ５０１ＸＧ８ｋｂ９ＶＺ７ｚ２３４]+")
        # if p.findall(word):
        #     continue
        if len(word) == 1 or len(word) == 0:
            continue
        f_result.write(word.strip("[").strip("]") + "\n")


def sortdict(dict, newdict):
    f_dict = open(dict, 'r', encoding="GB18030")
    f_new = open(newdict, 'w', encoding="GB18030")
    all_word = []
    for line in f_dict.readlines():
        line = line.strip()
        all_word.append(line)

    words = sorted(all_word)
    for i in words:
        f_new.write(i + "\n")
    f_new.close()
    f_dict.close()


def main():
    # rm_punctuation("199801_seg.txt", "none_punctuation.txt")
    # handle_dictfile("none_punctuation.txt", "dic.txt")
    sortdict("dic.txt", "sort_dic.txt")


if __name__ == '__main__':
    main()
