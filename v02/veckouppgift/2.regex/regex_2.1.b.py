"""
2 Öva på regex
1b Denna gången vill vi veta om det finns två längder.
"""

import re

lenghts = [44, False, 23, 5, "Noll", '127', None, 34]

for height, length in enumerate(lenghts, start=10):
    
    _s = f"Fiskarna som jag fångade var {length} cm långa och {height} cm höga."
    regex = r"(\d+.*cm).*(\d+.*cm)"
    
    if re.search(regex, _s):
        print(f"'{_s}'\t-> innehåller en längd och höjd i cm")
        continue
    
    print(f"'{_s}'\t-> innehåller INTE en längd och höjd i cm")