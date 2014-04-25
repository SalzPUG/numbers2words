#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from numbers2words import numbers2words

values = { 3: "drei",
           4: "viere",
           5: "fünfe",
           6: "sechse",
           7: "sieme",
           8: "achte",
           9: "neine"  }

tens = ['zehne', 'zwoanzge', 'dreißge', 'vierzge', 'fuchzge', 'sechzge',
        'siebzge', 'achtzge', 'neinzge']

def test_numbers2words_1():
    assert_equals(numbers2words(1), "oans")

def test_numbers2words_2():
    assert_equals(numbers2words(2), "zwoa")

def test_numbers2words_10():
    assert_equals(numbers2words(10), "zehne")

def test_numbers2words_hash():
    for key,val in values.items():
        assert_equals(numbers2words(key), val)

def test_numbers2words_tens():
    for index, val in enumerate(tens, 1):
        assert_equals(numbers2words(10 * index), val)

def test_numbers2words_11():
    assert_equals(numbers2words(11), "eife")

def test_numbers2words_12():
    assert_equals(numbers2words(12), "zweife")

def test_numbers2words_13():
    assert_equals(numbers2words(13), "dreizen")

def test_numbers2words_21():
    assert_equals(numbers2words(21), "oanazwanzg")

def test_numbers2words_33():
    assert_equals(numbers2words(33), "dreiadreißg")

def test_numbers2words_121():
    assert_equals(numbers2words(121), "hundatoanazwanzg")

def test_numbers2words_285():
    assert_equals(numbers2words(285), "zwoahundatfünfadochzg")

def test_numbers2words_minus1():
    assert_raises(ValueError, lambda: numbers2words(-1))
