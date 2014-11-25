#!/usr/bin/python
# -*- coding: UTF-8 -*-
while True:
    # if elif else语句
    score = input("Please input your score(0-100):")
    if(score >= 90) and (score <= 100):
        print "A"
    elif(score >= 80) and (score < 90):
        print "B"
    elif(score >= 60) and (score < 80):
        print "C"
    else:
         print "D"
