"""
1c Längderna ska vara samma enhet.
"Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."

Vad menar med samma enhet???
Exemplet ovan är det olika enheter eller tänker jag förmycket.

"""

import re

lenghts = [44, False, 23, 5, "Noll", '127', None, 34]

"""
for height, length in enumerate(lenghts, start=10):
    
    _s = f"Fiskarna som jag fångade var {length} cm långa och {height} cm höga."
    regex = r"(\d+.*cm).*(\d+.*cm)"
    
    if re.search(regex, _s):
        print(f"'{_s}'\t-> innehåller en längd och höjd i cm")
        continue
    
    print(f"'{_s}'\t-> innehåller INTE en längd och höjd i cm")
    
"""