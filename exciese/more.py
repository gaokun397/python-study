#!/usr/bin/env python

def more(text, numlines=15):
    lines = text.split('\n')
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print line
        if lines and raw_input('More?') not in ['Y', 'y']:
            break
if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(),10)
