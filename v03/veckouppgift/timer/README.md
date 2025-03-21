# TIMER-VUE

---

## TODO

- skapa och ta bort widgets \- timer och anteckning
- byta plats på två widgets
- ändra tidsinställning på timer
- starta, pausa, återställ
- ändra texten för anteckning
- ändra temafärg

Extra

- ändra nman på timers
- ändra så att timern räknar upp
- använd "clock" för att köra ner timern till 00:05 för att säkerställa
  - rosa färg
  - minus på klockan

---

## User Stories

**US01**  
som en användare  
vill jag kunna komma åt webbsidan  
så att jag kan använda den efter mina behov

**US02**  
som en användare  
vill jag kunna lägga till och ta bort widgets  
så att jag kan anpassa webbsidan efter mina behov

**US03**  
som en användare  
vill jag kunna flytta på widgets  
så att jag kan anpassa webbsidan efter mina behov

**US04**  
som en användare  
vill jag kunna ändra tiden på timern  
så att jag kan få en tid som passar mig och mina behov

**US05**  
som en användare  
vill jag kunna hantera timerna  
så att jag kan starta, stoppa och återställa timern efter mina behov

**US06**  
Som en användare  
vill jag kunna ändra texten på en anteckning  
så att jag kan anpassa anteckningen efter mina behov

**US07**  
som en användare  
vill jag kunna ändra färgern på webbsidan  
så att jag kan anpassa webbsidan efter behov

**US08**
Som en användare
vill jag kunna ändra rubriken på en timer
så att det framgår vad den är till för

---

## Acceptanskriterier

**US01.AC01**: Åtkomst till timer-vue webbsidan är möjligt  
**US01.AC02**: Att inga widgets finns på webbsidan när man börjar  
**US01.AC03**: Att det finns knappar att kunna lägga till anteckningar och timer.

**US02.AC01**: Lägg till en anteckning och en timer, ta sedan bort dem och webbsidan skall vara tom på widgets

**US03.AC01**: Lägg till en anteckning och en timer flytta sedan timern så att den hamnar överst
**US03.AC02**: Säkerställ att det fortfarande finns finns 2 stycken widgets på webbsidan

**US04.AC01**: Lätt till en timer och sedan ändra tiden på timern  
**US04.AC02**: Efter att en timer har anpassats skall den kunnas ta bort utan några problem

**US05.AC01**: Lägg till en timer, starta timern, stoppa timern, återställ timern

**US06.AC01**: Lägg till en anteckning och ändra texten

**US07.AC01**: Kontrollera de olika definerade theme knapparna på webbsidan så att theme ändras och knappen blir "selected"

**US08.AC01**: När en timer har skapas skall standard rubriken vara "Break"
**US08.AC02**: Rubriken på en timer skall kunna ändras

---

## Testscenarier

OBS!!! Det finns alltid en widget på webbsidan från början, ligger först och innehåller inget

**TS01** (US01.AC01, US01.AC02 och US01.AC03)  
01. Kontrollera att åtkomsten till webbsidan är möjlig  
02. Kontrollera att inga widgets finns från början på webbsidan  
03. Kontrollera att det finns 2 knappar på webbsidan som har namn som innehåller "Add"

**TS02** (US02.AC01)  
01. Kontrollera att inga widgets finns från början på webbsidan  
02. Klicka på knappen för att lägga till en timer  
03. Klicka på knappen för att lägga till en anteckning  
04. Kontrollera att 2 stycken widgets finns på webbsidan  
05. Klicka på knappen för att ta bort timern  
06. Klicka på knappen för att ta bort anteckning  
07. Kontrollera att inga widgets finns längre kvar på på webbsidan

**TS03** (US03.AC01 och US03.AC02)  
01. Klicka på knappen för att lägga till en anteckning  
02. Klicka på knappen för att lägga till en timer  
03. Kontrollera att anteckningar ligger överst  
04. Klicka på knappen för att flytta timern överst  
05. Kontrollera att timern ligger överst  
06. Kontrollera att 2 stycken widgets finns på webbsidan

**TS04** (US04.AC01 och US04.AC02)  
01. Klicka på knappen för att lägga till en timer  
02. Kontrollera att standard tiden är 15:00 minuter  
03. Ändra tiden till 01:00 minuter  
04. Kontrollera att den nya tiden är 01:00 minuter och att det bara finns en timer  
05. Kontrollera att det bara finns 1 widget finns på webbsidan

**TS05** (US05.AC01)  
01. Klicka på knappen för att lägga till en timer  
02. Kontrollera att standard tiden är 15:00 minuter  
03. Starta timern  
04. Vänta i 10 sekunder  
05. Stoppa timern  
06. Kontrollera att tiden har ändrat  
07. Återställ timern  
08. Kontrollera att standard tiden är 15:00 minuter

**TS06** (US06.AC01)  
01. Klicka på knappen för att lägga till en anteckning  
02. Kontrollera att standard texten, "Click to change text", är satt i anteckningen  
03. Visa "input field"  
04. Ändra texten på anteckningen till "Test text"  
05. Göm "input field"  
04. Kontrollera att anteckningen har fått det nya texten  
05. Kontrollera att det bara finns 1 widget finns på webbsidan

**TS07** (US07.AC01)  
01. Kontrollera att antalet theme knappar som är definerade stämmer med det förväntade antalet  
02. För varje knapp   
    * Klicka på den valda theme knappen  
    * Kontrollera att rätt "theme" på webbsidan aktiveras  
    * Kontrollera att knappen blir "selected"  

**TS08** (US08.AC01 och US08.AC02)  
01. Klicka på knappen för att lägga till en timer  
02. Kontrollera att standard rubriken vid en ny timer är "Break"  
03. Klicka på rubriken (inkl pennen) för att ett input fält skall dyka upp  
04. Ändra på rubriken till "Test"  
05. Kontrollera att den nya rubriken finns på timern  