#!/usr/bin/env python

try: set
except NameError: from sets import Set as set
def unique(s): 

    try:
        return list(set(s))
    except:
        pass
    t = list(s)
    try:
        t.sort()
    except typeError:
        del t
    else:
        return [x for i,x in enumerate(t) if not i or x !=t[i-1]]
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    return u
l=[1,1,2,3,4,22,33,33]
print unique(l)
