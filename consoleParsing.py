"""
This simple script shows how to use the library argparse
included within Python to start making a simple calculator.

Example use
###############
In the console:
python consoleParsing.py --add 1 -s 2 -d 4

In the debugger (pydb):
vars(args)

# Should return:
{'add': ['1'], 'sub': ['2'], 'div': ['4']}
###############
"""

import argparse

# Subclass ArgumentParser
parser = argparse.ArgumentParser(description="A simple calculator")

# Add possible arguments for console call of script
parser.add_argument("-a", '--add', nargs="+", help="Sums numbers")
parser.add_argument("-s", '--sub', nargs="+", help="Subtracts numbers")
parser.add_argument("-d", '--div', nargs="+", help="Divides numbers")

args = parser.parse_args()

breakpoint()
                        

