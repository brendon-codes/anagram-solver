LAST Anagram Solver
===================

Author: Brendon Crawford

Homepage: http://github.com/last/anagram/

This is a distributed/multi-core anagram solver.

Basic Usage:

    $ echo "hello world" | ./solve.py
    $ ./solve.py < some-input.txt

The optional "-w" argument specifies the number of
workers to use per CPU. The default is 2.

The optional "-j" argument specifies the number of
jobs to execute per worker. The default is 2.

Examples:

    $ echo "hello world" | ./solve.py -w 4 -j 4

The solver uses a dictionary wordlist which can be found
in "data/wordlist.txt". You can replace this with your own
word list if you wish.
