#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

mycart = (0, 10, -6, -7, 2, 5)
a = tuple(map(lambda x: abs(x), mycart[mycart.index(0):] ))
print(sum(a), min(a[1:]))
