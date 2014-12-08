#!/usr/bin/env python

formattor = "%r %r %r %r"

print formattor % (1,2,3,4)
print formattor % ("one","two","three","four")
print formattor % (True,False,False,True)
print formattor % (formattor,formattor,formattor,formattor)
print formattor % ("I had this thing.",
                   "That you could type up right.",
                   "But it didn't sing.",
                   "So I said goodnight.")
                
