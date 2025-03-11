"""
2 Öva på regex
1a Skriv ett regex som kontrollerar att det finns en längd i strängen, 
som anges i centimeter: "Fiskarna som jag fångade var 55 cm långa."
"""

import re

lenghts = [44, False, 23, 5, "Noll", '127', None, 34]

for length in lenghts:
    
    _s = f"Fiskarna som jag fångade var {length} cm långa."
    regex = "[0-9]+.cm"
    
    if re.search(regex, _s):
        print(f"'{_s}'\t-> innehåller en längd i cm")
        continue
    
    print(f"'{_s}'\t-> innehåller INTE en längd i cm")