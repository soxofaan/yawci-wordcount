#!/usr/bin/env python

import sys
import re

def output_key_value(key, value):
	sys.stdout.write('{k}\t{v}\n'.format(k=key, v=value))

def main(input = sys.stdin):
	word_rep = re.compile('\w+')
	for line in input:
		for match in word_rep.finditer(line.lower()):
			output_key_value(match.group(0), 1)

if __name__ == '__main__':
	main()
