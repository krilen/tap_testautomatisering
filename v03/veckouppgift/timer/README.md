# TIMER-VUE

---

## TODO

- skapa och ta bort widgets \- timer och anteckning
- byta plats på två widgets
- ändra tidsinställning på timer
- starta, pausa, återställ
- ändra texten för anteckning
- ändra temafärg

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

**US07.AC01**: Klicka på knapparna för att ändra färgen på webbsidan

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

**TS06** (US06.AC01)  
01. Klicka på knappen för att lägga till en anteckning  
02. Kontrollera att standard texten, "Click to change text", är satt i anteckningen  
03. Visa "input field"  
04. Ändra texten på anteckningen till "Test text"  
05. Göm "input field"  
04. Kontrollera att anteckningen har fått det nya texten  
05. Kontrollera att det bara finns 1 widget finns på webbsidan
