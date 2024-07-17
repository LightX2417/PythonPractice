# https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true

regex_pattern = r"[,.]"  

import re

print("\n".join(re.split(regex_pattern, input())))
