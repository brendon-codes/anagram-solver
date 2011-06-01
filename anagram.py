#!/usr/bin/env python

"""
LAST.vc Anagram Solver

Author: Brendon Crawford <brendon@last.vc>
"""

import os
import sys
import re


def main():
    """
    Main Routine from Command Line

    Returns: Int
    """
    data, orig_data = get_input_data()
    wordlist, lenmap = get_wordlist()
    out = cycle_all(data, wordlist, lenmap)
    show_results(out, orig_data)
    return 0


def show_results(out, orig_data):
    """
    Shows Results
    """
    print("Subject:\n%s\n" % orig_data)
    print("Anagram:\n%s\n" % out)
    return True


def get_input_data():
    """
    Get input data
    """
    orig_data = sys.stdin.read()
    data = re.sub(r'\s+', '', orig_data)
    return (data, orig_data)


def get_wordlist():
    """
    Gets wordlist
    """
    dname = os.path.dirname(__file__)
    fname = os.path.realpath(dname + '/data/wordlist.txt')
    fh = open(fname, 'r')
    wordlist = frozenset([x.rstrip() for x in fh])
    fh.close()
    lenmap = {}
    for word in wordlist:
        wordlen = len(word)
        if wordlen not in lenmap:
            lenmap[wordlen] = []
        lenmap[wordlen].append(word)
    return (wordlist, lenmap)


def cycle_all(data, wordlist, lenmap):
    """
    Cycle
    """
    found_words = []
    bucket = ''
    word = data
    while len(word) > 0:
        found_word = find_match(word, wordlist, lenmap)
        if found_word is None:
            word, extra = extract_word(word)
            bucket += extra
        else:
            found_words.append(found_word)
            word = bucket
            bucket = ''
    out = build_output(found_words)
    return out


def build_output(found_words):
    """
    Builds output string
    """
    random.shuffle(found_words)
    out = ' '.join(found_words)
    return out


def find_match(word, wordlist, lenmap):
    """
    Find a match of word against wordlist
    """
    wordlen = len(word)
    sword = sorted(word)
    if wordlen in lenmap:
        for target_word in lenmap[wordlen]:
            ismatch = (sword == sorted(target_word))
            if ismatch:
                return target_word
    return None


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
