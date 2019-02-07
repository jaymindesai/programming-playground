# Beautification Score

import re
from collections import defaultdict, Counter

def bscore(s):
    # _bscore(s)
    freq = Counter(re.findall('[a-z]', s.lower(), re.I))
    mx = 26
    score = 0
    for _, f in freq.most_common():
        score += f * mx
        mx -= 1

    return score

def _bscore(s):
    freq = defaultdict(int)
    for c in s:
        if re.match('[a-z]', c, re.I):
            freq[c.lower()] += 1
    mx = 26
    score = 0
    for f in sorted(freq.values(), reverse=True):
        score += f * mx
        mx -= 1

    return score


ip = input().strip()
print(bscore(ip))
