#!/usr/bin/env python

from random import choice
import string

def GenPasswd(length=8,chars=string.letters+string.digits):
    return ''.join([ choice(chars) for i in range(length)])

for i in range(10):
    print GenPasswd(12)
