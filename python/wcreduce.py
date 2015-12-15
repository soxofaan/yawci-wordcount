#!/usr/bin/env python

import sys


def output_key_value(key, value):
    sys.stdout.write('{k}\t{v}\n'.format(k=key, v=value))


def read(input=sys.stdin):
    for line in input:
        try:
            word, count = line.split('\t', 1)
            yield word, int(count)
        except StandardError:
            print >>sys.stderr, 'Ignoring', repr(line)


def main(input=sys.stdin):
    prev_word = None
    total = 0
    for word, count in read(input=input):
        if word == prev_word:
            total += count
        else:
            if prev_word is not None:
                output_key_value(prev_word, total)
            prev_word = word
            total = count

    output_key_value(prev_word, total)


if __name__ == '__main__':
    main()
