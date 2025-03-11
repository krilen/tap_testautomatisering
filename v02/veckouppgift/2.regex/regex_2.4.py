"""
4. Skriv ett regex som matchar ett pengavärde i siffror. 
Exempel på värden som ska matchas:
 * 200 kr
 * 12,50 kr
 * 0,35 kr

"""


import re

amounts = ["$200", "200 kr", "12,50 kr", "0,35 kr", "12,50 €", "0.35 kr"]


for amount in amounts:
    regex = r"^(\d+,)?\d*.kr$" # => "x,x kr" / "x kr"
    
    if re.search(regex, amount):
        print(f"'{amount}' -> är ett korrekt pengavärde")
        continue
    
    print(f"'{amount}' -> är INTE ett korrekt pengavärde")