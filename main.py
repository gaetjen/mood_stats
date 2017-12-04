#!/usr/bin/python3
import sys
import time
from collections import Counter

file_path = '/home/johannes/0/programs/tagtime/jo_mood.log'
ignore = ['afk', 'off', 'RETRO']
min_num = 1
if len(sys.argv) == 1:
    min_ts = 0
elif len(sys.argv) >= 2:
    min_ts = time.time() - int(sys.argv[1]) * 24 * 60 * 60
if len(sys.argv) >= 3:
    min_num = int(sys.argv[2])

with open(file_path, "r") as file:
    lines = [line.split() for line in file]

all_moods = []
[all_moods.extend(l[1:-3]) for l in lines if int(l[0]) >= min_ts]
cnt = Counter(all_moods)
for c, n in cnt.most_common():
    if n < min_num:
        break
    if c not in ignore:
        print(n, c)
