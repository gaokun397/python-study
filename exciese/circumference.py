#!/usr/bin/env python

import math
radiusString = raw_input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)

print "The cirumference is:",circumference,",and the area is :",area
