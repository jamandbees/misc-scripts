#!python

import sys
import os

file = sys.stdin

# Ultimately we create a big old buffer and reverse it.

def help():
    return """
Usage: tac filename 
cat foo | tac

Reverses lines from either stdin or a file

-h --help - displays this help message
"""


if "-h" in sys.argv or "--help" in sys.argv:
    print(help())
    sys.exit(1)

try:
    if (sys.argv[1]):
        file = sys.argv[1]
        if (os.path.exists(file)):
            file = open(file)
        else:
            sys.stderr.write(help())
            sys.exit(2)
except IndexError:
    pass


# If we haven't already filled buffer, assume we're reading from stdin.

tac = list(reversed(file.readlines()))

for line in tac:
    if line:
        print(line, end = '')
