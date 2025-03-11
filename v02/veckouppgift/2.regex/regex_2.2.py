"""
2 Skriv ett regex som matchar ett svenskt postnummer. Postnummer består av fem 
siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45"
Om du vill övertänka fördjupa dig mera: https://sv.wikipedia.org/wiki/Postnummer_i_Sverige 
"""

import re

postnumbers = ["111 20", "21 124", "211 24", "411 03", "40 903", "621 52", "Borås", "751 21", "905 32"]


for postnumber in postnumbers:
    
    regex = r"^\d{3}.\d{2}$"
    
    if re.search(regex, postnumber):
        print(f"'{postnumber }'\t-> är ett korrekt postnummer")
        continue
    
    print(f"'{postnumber}'{ '\t' if len(postnumber) < 6 else ''}\t-> är INTE ett korrekt postnummer")