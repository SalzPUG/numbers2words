#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numbers2words import numbers2words

print "zoi,nom"
for number in range(1, 1000):
    try:
        word = numbers2words(number)
    except Exception as e:
        word = "Exception(%s)" % type(e).__name__

    print "%d,%s" % (number, word)
