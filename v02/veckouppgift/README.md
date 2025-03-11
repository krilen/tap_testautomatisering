# Veckouppgift 2

## Vecka 11, 10/3

*1 Du ska lösa uppgiften självständigt eller tillsammans med en annan student. Men vid minst ett tillfälle ska du göra code review i en grupp.*

*2 Du får ta hjälp av AI för att förklara koncept och lösa fel. Du får inte be AI lösa uppgiften åt dig direkt. Om du gör det, kommer du inte att lära dig grunderna, och inte kunna lösa svårare problem.*

---

### 1 Diskutera i grupp

*Denna gången är det en fördel att diskutera de flesta uppgifterna.*  
*Planera din tid, så att du hinner arbeta med **alla** övningarna. Du ska alltså inte göra "färdigt" alla tidigare övningar innan du går vidare på nästa.*

1a Vilka strängar matchas av det reguljära uttrycket: "ab" ? Testa era svar på [https://regex101.com/](https://regex101.com/) 

1. "a b"  
2. "aBBa"  
3. "sabotör"

1b Betrakta uttrycket "nisse". Vad skriver jag för att matcha både "Nisse", "NISSE" och "nisse"?

1c Vilka strängar matchas av "a\*n" ?

1. "an"  
2. "amerikan"  
3. "naturlig"  
4. "annandag"

1d Vilka strängar matchas av "\[ae\]n" ?

1. "naiv"  
2. "inconsequential"  
3. "bae"

1e Vilka strängar matchas av "je.+e"?

1. "je"  
2. "jee"  
3. "jeppe"  
4. "je je"

1f Vilka strängar matchas av "\\san?\\s"

1. "sansad"  
2. " annan "  
3. "    an   na   an   "  
4. "be a darling"

1e Skriv ner med egna ord, vad följande uttryck matchar. "Strängar som innehåller…"

1. "lines?"  
2. "^a\*ö$"  
3. "\[aeiouyåäö\]+"  
4. "\[123456789\]\\d\*"  
5. "\\d{4}-\\d{2}-\\d{2}

2a Betrakta [https://lejonmanen.github.io/agile-helper/](https://lejonmanen.github.io/agile-helper/) . Skriv en user story som beskriver att användaren ska kunna läsa hur man gör en "sprint retrospective".

2b Skriv ner ett testscenario för user storyn. Använd en punktlista. Fundera särskilt på vad som ska testas *implicit* och *explicit*.  
Implicit \= underförstått, testas indirekt  
Explicit \= uttryckligen, testas direkt

3 Titta på kodexemplet från lektionen. Skriv upp allt du är osäker på och diskutera i grupp eller fråga om på nästa lektion.

def test\_view\_sprint\_planning(page: Page):  
    """Testa att det går att se Sprint planning"""  
    page.goto("https://lejonmanen.github.io/agile-helper/")

    \# Klicka på button "First"  
    locator \= page.get\_by\_role("button")  
    first\_button \= locator.get\_by\_text("First")  
    first\_button.click(timeout\=100)

    \# Hitta button med texten "Sprint planning"  
    sp\_button \= page.get\_by\_role("button").get\_by\_text(re.compile("Sprint planning"))  
    expect(sp\_button).to\_be\_visible()  
      
    \# Klicka på den  
    sp\_button.click(timeout\=100)

    \# Finns rubriken "Sprint planning"?  
    sp\_heading \= page.get\_by\_role("heading").get\_by\_text("Sprint planning")  
    expect(sp\_heading).to\_be\_visible()

---

### 2 Öva på regex

1a Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter:  
"Fiskarna som jag fångade var 55 cm långa."

1b Denna gången vill vi veta om det finns två längder.

1c Längderna ska vara samma enhet.  
"Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."

2 Skriv ett regex som matchar ett svenskt postnummer. Postnummer består av fem siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45"  
Om du vill ~~övertänka~~ fördjupa dig mera: [https://sv.wikipedia.org/wiki/Postnummer\_i\_Sverige](https://sv.wikipedia.org/wiki/Postnummer_i_Sverige) 

3 Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601, alltså 10 tecken med bindestreck mellan avdelningarna. Exempel: 2025-03-10.

4 Skriv ett regex som matchar ett pengavärde i siffror. Exempel på värden som ska matchas:

* 200 kr  
* 12,50 kr  
* 0,35 kr

5a Skriv ett regex som matchar en e-postadress (användarnamn@server.domän) enligt följande icke kompletta regler.

* användarnamn kan innehålla bokstäver, siffror och specialtecknen som punkt och bindestreck  
* server kan innehålla samma sorts tecken  
* domän kan innehålla bokstäver och siffror

5b Gör ett regex som matchar en komplett e-postadress enligt specifikationen i artikeln här:  
[What is a valid email address format](https://snov.io/knowledgebase/what-is-a-valid-email-address-format/) 

Träna mer på regex: [Regex Golf](https://alf.nu/RegexGolf?world=regex) (svår)

---

### 3 Öva på user stories

Skapa user stories som beskriver funktionaliteten i [https://lejonmanen.github.io/agile-helper/](https://lejonmanen.github.io/agile-helper/)   
För varje user story ska du skriva ett scenario. Målet är att all befintlig funktionalitet ska täckas in av en user story \- alla knappar ska bli klickade minst en gång.  
Gör gärna den här uppgiften tillsammans med klasskamrater, så ni kan diskutera era scenarion, skillnader och likheter.

Exempel:  
\[User story 1\]  
**Story**: Som en användare, vill jag se mötet "sprint planning" som utspelar sig första dagen på en sprint, så att jag vet vad jag ska göra på mötet.

**Scenario**:

1. Navigera till webbsidan https://lejonmanen.github.io/agile-helper/   
2. Klicka på knappen med texten "First"  
3. Klicka på knappen vars text innehåller "Sprint planning"  
4. Kontrollera att ett \<dialog\> element visas på sidan, som innehåller en rubrik med texten "Sprint planning"

---

### 4 Öva på E2E test

Utgå från dina user stories och scenarion i föregående uppgift. Skriv kod med Playwright som testar dem. Ta hjälp av kodexemplet i presentationen.

---

.