#!/usr/bin/python

#import argparse
#import random
#import hashlib
import string
import re
from collections import defaultdict

eventlog = 'events.log'

# [2018-04-11   03:13:57]  OK
# [2018-04-11   03:14:04]  OK
# [2018-04-11 03:14:04] NOK
# [2018-04-11 03:14:09] OK

minutecodes = defaultdict(int)

def doeventlogparse():
#    log_pattern = re.compile('^[^\[]+\[([^\s]+)\s+([\d]{2}:[\d]{2}):[\d]{2}\]\s+(\w+)')
    log_pattern = re.compile('^[^\[]*\[([^\s]+)\s+([\d]{2}:[\d]{2}):[\d]{2}\]\s+(\w+)')

    with open(eventlog, 'r') as events:
        for line in events:
            if groups := log_pattern.match(line):
                date = groups.group(1)
                minute = groups.group(2)
                code = groups.group(3)
                if code == 'NOK':
                    dateminute = date + ' ' + minute
                    minutecodes[dateminute] += 1

    for minute in minutecodes.keys():
        print(minute, minutecodes[minute])

if __name__ == '__main__':
    doeventlogparse()
