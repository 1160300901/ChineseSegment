#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: sunyueqing
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: sunyueqinghit@163.com
@File : Score.py
@Time : 2018/12/2 16:19
@Site : 
@Software: PyCharm
'''

'''
3.3 正反向最大匹配分词性能分析 
生成score.txt文件(包括准确率（precision）、召回率（recall）， F 值的结果文件)
 
'''


def answer_word(purefile):
    '''
    统计分词标准文件的正确词数
    :param purefile: 分词标准文件
    :return: 正确词数
    '''
    f_pure = open(purefile, "r", encoding="GB18030")
    counter = 0
    for line in f_pure.readlines():
        i = line.count('/')
        counter = counter + i
    return counter


def right_word(purefile, MMfile):
    '''
    与标准分词文件相比，正、反向分词结果的正确词数
    :param purefile: 标准分词文件
    :param MMfile: 正、反向分词结果
    :return: 正确词数
    '''
    f_pure = open(purefile, "r", encoding="GB18030")
    f_MM = open(MMfile, "r", encoding="GB18030")
    counter = 0
    for pure_line in f_pure.readlines():
        MM_line = f_MM.readline().split("/ ")
        MM_line = [x for x in MM_line if x != '\n']
        pure_line = pure_line.split("/ ")
        pure_line = [x for x in pure_line if x != '\n']
        tmp = [l for l in MM_line if l in pure_line]
        counter += len(tmp)
    return counter


def main():
    # 训练集评分，结果写入文件"train_data/train_score.txt"中
    # f_score = open("train_data/train_score.txt", "w")
    # standard_words = answer_word("train_data/199801_seg.txt")
    # print("standard_words: ", standard_words)
    # FMM_all_words = answer_word("train_data/seg_FMM.txt")
    # print("FMM_all_words: ", FMM_all_words)
    # FMM_right_words = right_word("train_data/199801_seg.txt", "train_data/seg_FMM.txt")
    # print("FMM_right_words: ", FMM_right_words)
    # FMM_Precision = FMM_right_words / FMM_all_words
    # FMM_Recall = FMM_right_words / standard_words
    # FMM_F = 2 * FMM_Precision * FMM_Recall / (FMM_Precision + FMM_Recall)
    # f_score.write(
    #     "FMM  " + "Precision: " + str(FMM_Precision) + ", Recall: " + str(FMM_Recall) + ", F: " + str(FMM_F) + "\n")
    #
    # BMM_all_words = answer_word("train_data/seg_BMM.txt")
    # print("BMM_all_words: ", BMM_all_words)
    # BMM_right_words = right_word("train_data/199801_seg.txt", "train_data/seg_BMM.txt")
    # print("BMM_right_words: ", BMM_right_words)
    # BMM_Precision = BMM_right_words / BMM_all_words
    # BMM_Recall = BMM_right_words / standard_words
    # BMM_F = 2 * BMM_Precision * BMM_Recall / (BMM_Precision + BMM_Recall)
    # f_score.write(
    #     "BMM  " + "Precision: " + str(BMM_Precision) + ", Recall: " + str(BMM_Recall) + ", F: " + str(BMM_F) + "\n")
    #
    #
    # f_score.close()

    # 测试集评分，结果写入文件"test_data/score.txt"中
    f_score = open("test_data/test_score.txt", "w")
    standard_words = answer_word("test_data/seg.txt")
    print("standard_words: ", standard_words)
    FMM_all_words = answer_word("test_data/seg_FMM.txt")
    print("FMM_all_words: ", FMM_all_words)
    FMM_right_words = right_word("test_data/seg.txt", "test_data/seg_FMM.txt")
    print("FMM_right_words: ", FMM_right_words)
    FMM_Precision = FMM_right_words / FMM_all_words
    FMM_Recall = FMM_right_words / standard_words
    FMM_F = 2 * FMM_Precision * FMM_Recall / (FMM_Precision + FMM_Recall)
    f_score.write(
        "FMM  " + "Precision: " + str(FMM_Precision) + ", Recall: " + str(FMM_Recall) + ", F: " + str(FMM_F) + "\n")

    BMM_all_words = answer_word("test_data/seg_BMM.txt")
    print("BMM_all_words: ", BMM_all_words)
    BMM_right_words = right_word("test_data/seg.txt", "test_data/seg_BMM.txt")
    print("BMM_right_words: ", BMM_right_words)
    BMM_Precision = BMM_right_words / BMM_all_words
    BMM_Recall = BMM_right_words / standard_words
    BMM_F = 2 * BMM_Precision * BMM_Recall / (BMM_Precision + BMM_Recall)
    f_score.write(
        "BMM  " + "Precision: " + str(BMM_Precision) + ", Recall: " + str(BMM_Recall) + ", F: " + str(BMM_F) + "\n")


    f_score.close()


if __name__ == '__main__':
    main()
