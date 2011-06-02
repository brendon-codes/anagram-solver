#!/usr/bin/env python

"""
LAST.vc Anagram Solver

Author: Brendon Crawford <brendon@last.vc>
"""

import os
import sys
import re
import random
import multiprocessing as mp
from optparse import OptionParser


def main():
    """
    Main routine from command line

    Returns: bool
    """
    options, _ = _get_options()
    orig_data = _get_input_data()
    out, score = runner(orig_data, options.workers, options.jobs)
    _show_results(out, orig_data, score)
    return True


def runner(orig_data, workers=2, jobs=2):
    """
    Runs solvers. Useful for testing. main() wraps around this

    Arguments:
        orig_data -- string
        workers -- int
        jobs -- int

    Returns: tuple(string, float)
    """
    data = _get_clean_data(orig_data)
    if len(data) == 0:
        out = ''
        score = 0.0
    else:
        wordlist, lenmap = _get_wordlist()
        out = _solver(workers, jobs, data, wordlist, lenmap)
        score = _get_score(out, data)
    return (out, score)


def _get_clean_data(orig_data):
    """
    Gets cleaned input data

    Arguments:
        orig_data -- string

    Returns: string
    """
    data = re.sub(r'[^a-zA-Z]', '', orig_data)
    return data


def _get_options():
    """
    Get command line options

    Returns: tuple(object, list)
    """
    usage = 'Usage: echo "input phrase" | %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-w', '--workers', type='int', dest='workers',
                      default=2, help="Workers per CPU")
    parser.add_option('-j', '--jobs', type='int', dest='jobs',
                      default=2, help="Jobs per worker")
    options, args = parser.parse_args()
    return (options, args)


def _solver(workers, jobs, data, wordlist, lenmap):
    """
    Starts job workers

    Arguments:
        workers -- int
        jobs -- int
        data -- string
        wordlist -- frozenset
        lenmap -- dict

    Returns: string
    """
    p_count = workers * mp.cpu_count()
    j_count = p_count * jobs
    pool = mp.Pool(processes=p_count)
    results = [pool.apply_async(_cycle_all, [data, wordlist, lenmap])
               for i in xrange(j_count)]
    resvals = [r.get() for r in results]
    bestchoice = reduce(lambda a, b: a if len(a) > len(b) else b, resvals)
    return bestchoice


def _get_score(out, data):
    """
    Gets score percentage value

    Arguments:
        out -- string
        data -- string

    Returns: float
    """
    out_clean = re.sub(r'\s+', '', out)
    score = ((float(len(out_clean)) / float(len(data))) * 100)
    return score


def _show_results(out, orig_data, score):
    """
    Prints results to console

    Arguments:
        out -- string
        orig_data -- string
        score -- float

    Returns: bool
    """
    print
    print("Subject:\n%s\n" % orig_data)
    print("Anagram:\n%s\n" % out)
    print("Score:\n%0.2f%%" % score)
    print
    return True


def _get_input_data():
    """
    Get input data from stdin

    Returns: string
    """
    orig_data = sys.stdin.read().strip()
    return orig_data


def _get_wordlist():
    """
    Gets wordlist and builds wordlist mappers

    Returns: tuple(frozenset, dict)
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


def _cycle_all(data, wordlist, lenmap):
    """
    Cycles through data

    Arguments:
        data -- string
        wordlist -- frozenset
        lenmap -- dict

    Returns: string
    """
    found_words = []
    bucket = ''
    word = data
    while len(word) > 0:
        found_word = _find_match(word, wordlist, lenmap)
        if found_word is None:
            word, extra = _extract_word(word)
            bucket += extra
        else:
            found_words.append(found_word)
            word = bucket
            bucket = ''
    out = _build_output(found_words)
    return out


def _build_output(found_words):
    """
    Builds output string

    Arguments:
        found_words -- list

    Returns: string
    """
    random.shuffle(found_words)
    out = ' '.join(found_words)
    return out


def _find_match(word, wordlist, lenmap):
    """
    Find a match of word against wordlist

    Arguments:
        word -- string
        wordlist -- frozenset
        lenmap -- dict

    Returns: string|None
    """
    wordlen = len(word)
    sword = sorted(word)
    if wordlen in lenmap:
        for target_word in lenmap[wordlen]:
            ismatch = (sword == sorted(target_word))
            if ismatch:
                return target_word
    return None


def _extract_word(data):
    """
    Extract word from string

    Arguments:
        data -- string

    Returns: tuple(string, string)
    """
    out = ''
    idx = random.randint(0, len(data) - 1)
    for i in xrange(len(data)):
        if i != idx:
            out += data[i]
    return (out, data[idx])


if __name__ == '__main__':
    """
    Run from command line
    """
    sys.exit(0 if main() else 1)
