#!/usr/bin/env python
while True:

        year=raw_input('please input a year: ')
        a= int(year)
        if a%4==0 and a%100!=0:
            print year, 'is runnian'
        elif a%400==0:
            print year ,'is runnian'
        else:
            print year ,'is not runnian'
