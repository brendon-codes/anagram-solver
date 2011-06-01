#!/usr/bin/env python

"""
LAST.vc Anagram Solver

Author: Brendon Crawford <brendon@last.vc>
"""

import os
import sys


def main():
    """
    Main Routine from Command Line

    Returns: Int
    """
    data = sys.stdin.read()
    wordlist = get_wordlist()
    cycle(data, wordlist)
    return 0


def get_wordlist():
    """
    Gets wordlist
    """
    dname = os.path.dirname(__file__)
    fname = os.path.realpath(dname + '/data/wordlist.txt')
    fh = open(fname, 'r')
    wordlist = [x.rstrip() for x in fh]
    fh.close()
    return wordlist


def cycle(data, wordlist):
    """
    Cycle
    """
    bucket = ''
    word = data
    while len(data) > 0:
        
        word, extra = extract_word(data)
        bucket += extra
    return True


def find_match(word):
    


def extract_word(data):
    """
    Extract word
    """
    out = ''
    idx = random.randint(0, len(data))
    for i in xrange(len(data)):
        if i != idx:
            out += data[i]
    return (out, data[idx])


if __name__ == '__main__':
    sys.exit(main())
