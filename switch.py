#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division

x = 1
y = 2
operator = "/"
result = {
    "+" : x + y,
    "-" : x - y,
    "*" : x * y,
    "/" : x / y
}
print result.get(operator)
operator1 = "+"
operator2 = "-"
operator3 = "*"
print result.get(operator1)
print result.get(operator2)
print result.get(operator3)
