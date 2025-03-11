"""
3 Skriv ett regex som matchar ett datum skrivet enligt den internationella
standarden ISO 8601, alltså 10 tecken med bindestreck mellan avdelningarna. 
Exempel: 2025-03-10.
"""

import re

dates = ["2025-03-11", "11/03/2025", "03-11-2025", "March 11, 2025", "2022-08-07", 
         "2025/03/11", "11-Mar-2025", "Tuesday, March 11, 2025", "2025.03.11", 
         "03.11.2025", "11.03.2025", "Mar 11, 2025", "2025-12-15"]


for _date in dates:
    regex = r"^\d{4}-\d{2}-\d{2}$"
    
    if re.search(regex, _date):
        print(f"'{_date}' -> är ett ISO 8601 datum")
        continue
    
    print(f"'{_date}' -> är INTE ett ISO 8601 datum")