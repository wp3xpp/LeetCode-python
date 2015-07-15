#! /bin/bash 
# -*- coding:utf-8 -*-

'''
一个教授逻辑学的教授，有三个学生，而且三个学生均非常聪明！
一天教授给他们出了一个题，教授在每个人脑门上贴了一张纸条并告诉他们，每个人的纸条上都写了一个正整数，且某两个数的和等于第三个！（每个人可以看见另两个数，但看不见自己的） 
教授问第一个学生：你能猜出自己的数吗？回答：不能
问第二个，不能
第三个，不能
再问第一个，不能
第二个，不能
第三个：我猜出来了，是144！
教授很满意的笑了。
请问您能猜出另外两个人的数吗？

请问： 第三个人是怎么猜出来的？你是怎么猜出另外两个数的？
'''
__author__ = 'FreeMind'

class Solution:

    def __init__(self, rounds, person, number):
        self.rounds = rounds
        self.person = person
        self.number = number
    
    def solution(self):
        if self.rounds == 1:
            if self.person == 1:
                return [[2, 1, 1]]
            elif self.person == 2:
                return [[1, 2, 1], [2, 3, 1]]
            else:
                return [[1, 1, 2], [2, 1, 3], [1, 2, 3], [2, 3, 5]]
        a = [[2, 1, 1]]
        b = [[1, 2, 1], [2, 3, 1]]
        c = [[1, 1, 2], [2, 1, 3], [1, 2, 3], [2, 3, 5]]
        results = [a, b, c]
        iterationNumber = (self.rounds - 2) * 3 + self.person 
        for i in range(iterationNumber):
            if i % 3 == 0:
                results[0] = [[x[1]+x[2], x[1], x[2]] for x in results[1] + results[2]]
            elif i % 3 == 1:
                results[1] = [[x[0], x[0]+x[2], x[2]] for  x in results[0] + results[2]]
            else:
                results[2] = [[x[0], x[1], x[0]+x[1]] for x in results[0] + results[1]]
        return results[self.person-1]
    def __str__(self):
        result = filter(lambda x:not self.number%max(x), self.solution())
        result = map(lambda x:[x[0]*self.number/sum(x)*2, x[1]*self.number/sum(x)*2, x[2]*self.number/sum(x)*2],result)
        res = ''
        for i in result:
            res += str(i)+"\n"
        return res.replace('[','(').replace(']', ')')
    __repr__ = __str__
            

if __name__ == '__main__':
    print Solution(2, 3, 144) #对应位置参数分别为轮数，最先知道答案的人，所知结果
    ##  print:
    ## (108, 36, 144)
    ## (64, 80, 144)
    ## (54, 90, 144)
    ## (36, 108, 144)
    ## (32, 112, 144)
        

    
