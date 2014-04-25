#!/usr/bin/env python
# -*- coding: utf-8 -*-

specials = {
    1: "oans", 2: "zwoa", 3: "drei",
    4: "viere", 5: "fünfe", 6: "sechse",
    7: "sieme", 8: "achte", 9: "neine",
    10: "zehne", 11: "eife", 12: "zweife",
    13: "dreizen"
}

tens = ['zehne', 'zwoanzge', 'dreißge', 'vierzge', 'fuchzge', 'sechzge',
        'siebzge', 'achtzge', 'neinzge']

values_ez = ['oana', 'zwoara', 'dreia', 'viera', 'fünfa', 'sechsa', 'simma',
             'ochta', 'neina']

values_tz = ['zen','zwanzg', 'dreißg', 'vierzg', 'fuchzg', 'sechzg',
        'siebzg', 'dochzg', 'neinzg']

values_hz = ['hundat','zwoahundat','dreihundat','viahundat','fünfhundat',
             'sechshundat', 'siebnhundat','ochthundat','neihundat']

def numbers2words(number):
    output = ''

    if number < 0:
        raise ValueError('is zkloa')

    if number > 100:
        hz, number = divmod(number,100)
        output += values_hz[hz - 1]

    if number > 13:
        if number % 10 == 0:
            output += tens[number / 10 - 1]
        else:
            tz, ez = divmod(number,10)
            output += values_ez[ez-1] + values_tz[tz-1]
    else:
        output = specials[number]
    return output

if __name__ == "__main__":
    import nose
    nose.main()
