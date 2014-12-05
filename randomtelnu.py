#!/usr/bin/env python

import random
for  x in range(10):
    randomnu=random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
    print x,randomnu

