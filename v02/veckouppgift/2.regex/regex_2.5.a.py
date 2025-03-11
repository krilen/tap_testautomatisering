"""
5a Skriv ett regex som matchar en e-postadress (användarnamn@server.domän)
enligt följande icke kompletta regler.
 * användarnamn kan innehålla bokstäver, siffror och specialtecknen som punkt och bindestreck
 * server kan innehålla samma sorts tecken
 * domän kan innehålla bokstäver och siffror

användarnamn@server.domän

"""

import re

emails = [ "john-mike.doe@example.com", "jane.smith@fictionalmail.com","@mail.com",
    "alex.miller@imaginary.domain.org", "lucy.green@fake-mail.net", "john@com"]

for email in emails:
    regex = r"[a-z0-9\.-]+@[a-z0-9/.-]+\.[a-z0-9]+"
    
    if re.search(regex, email):
        print(f"'{email}' -> är av korrekt format")
        continue
    
    print(f"'{email}' -> är INTE av korrekt format")
    
    
    