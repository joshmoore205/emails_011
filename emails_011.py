#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip()
  i = 0
  while i < len(line) and not ("0" <= line[i] and line[i] <= "9"):
    i += 1
  if i < len(line):
    new = line[0:i]
    new = new.split(".")
    print(new[0] + " " + new[1])
