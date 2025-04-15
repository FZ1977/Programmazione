#!/usr/bin/python

import os
import sys

file=open(sys.argv[1],'r')
print file.read().find('testo')
