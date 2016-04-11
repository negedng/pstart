#!/usr/bin/env python

"""
    Németh Gergely Dániel

    Python 3 character counter

    Counts the characters of the std input, and prints the numbers of hungarian characters
"""

import sys
import collections


def main():
    """Counts the caracters of std input data"""
    # python version 3+
    print(sys.version)

    # read lines of stdin
    for line in sys.stdin:
        # python 3 reads in unicode, no decode needed
        line = line.rstrip()  # cuts eol character
        line = line.lower()  # lower the letters
        dic = {}  # dictionary for the letters
        for letter in line:
            if (dic.get(letter) == None):
                # first of this letter, make new dict row
                dic[letter] = 1
            else:
                dic[letter] += 1

        # Show the result in the output

        # simple dictionary print
        # print dic

        # default OrderedDict sort
        # it sorts by coding not language order
        # od = collections.OrderedDict(sorted(dic.items()))
        # for k, v in od.items():
        #     print(k+'\t'+str(v))

        # Use the Hungarian letters
        hunletters = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"
        for l in hunletters:
            if (dic.get(l) != None):
                print(l+'\t'+str(dic.get(l)))




if __name__ == '__main__':
    main()

