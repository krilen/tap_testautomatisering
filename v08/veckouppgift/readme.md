# Veckouppgift CI/CD
## Vecka 8 i Testautomatisering och testverktyg

**Krister Lenberg, 2025apr24**

### Uppgift
1. Beskriv ett CI/CD-flöde för ett tänkt projekt (till exempel en Flask-app eller webbtjänst).
   a. Vad händer när utvecklaren pushar kod?  
   b. Vilka tester ska köras?  
   c. När och hur byggs applikationen?  
   d. Rita flödet som en enkel bild eller lista.  
   e. Vad skulle kunna gå fel i flödet?  
   f. Vilka tester är viktigast i just ditt flöde?  
   g. Hur kan testning förbättra kvaliteten?  
2. Hur tror du att automatiserad testning påverkar en utvecklares vardag?
3. Vad är en fördel och en nackdel med att ha testning inbyggd i CI/CD-flödet?
4. Om du skulle införa CI/CD i ett skarpt projekt – vad skulle du börja med?
5. Hur skiljer sig GitHub Actions från andra CI/CD-verktyg du hört om eller testat?  
   (denna gör du bara om du har erfarenhet från andra CI/CD-verktyg).
   
### Svar
När ett nytt projekt skapas bör ett CI/CD flöde sättas upp dock i början av projektet (applikationen) finns inte behovet att göra någon typ av deployment. Allt innan deployment är bra om det sätts upp i början därefter när projektet löper på kan CI/CD flödet utökas och tillslut kan även deployment ingå. Vid utveckling men jämna mellanrum speciellt när nya delar delar eller funktioner läggs till bör "commits" göras för att kunna få en bra översyn på historiken dock är det inte förrän en push (eller pull request) av koden till repository som innehåller CI/CD flödet som CI/CD födet aktiveras.

De tester som skall köras på applikationen är först och främst unit tester som har direkt koppling till koden. Därefter skall olika typer av integrations tester köras för att kontrollera hur utvecklarens kod interagerar med annan kod och andra utvecklares kod. Om något går fel i dessa tester skall detta kontrolleras och åtgärdas snarast.  
Andra uppsatta kontroller som Linting på hur syntaxen för koden böra vara kan också ske. Oftast sker det en automatiskt kontroll av kodens definierade "dependencies" så att eventuella risker informeras om så att utvecklaren kan åtgärda det genom att uppgradera eller ändra kodens "dependencies" om det inte sker automatisk bör man ändå säkerställa att detta ändå sker på något sätt.

Enligt mig är utvecklarens egna tester, unit tester samt de integrations tester som utvecklaren själv ansvarar för som är viktigast eftersom de skall vara ett bevis på att koden uppfyller de krav och mål som är uppsatta. Därefter är det integrations tester mellan olika utvecklare som är viktiga dvs hur utvecklarens kod interagerar med andra utvecklares kod. Dock kan det ju vara så att denna kod inte finns tillgänglig i början av utvecklingen för andra utvecklare att göra integrations tester med, därför är det viktigt att i dessa fall att "mock" kod tas fram av den andra utvecklaren för integrations tester skall kunna utföras tills dess att riktiga integrations tester kan göras mellan olika utvecklares kod. På detta sätt vet man som utvecklare hur en annans utvecklares kod kommer att reagera dvs vad som förväntas av en (input) och vad för återkoppling (output) man får, när väl all kod är utvecklad skall det inte vara någon skillnad.

Om alla de olika automatiserade testerna som man satt upp i CI/CD flödet ger ett positivt resultat skall flödet fortsätta till nästa steg. Annars skall det ta stop och då får utvecklaren kontrollera och eventuellt åtgärda problem. Det kan ju vara så att problemet inte ligger i ens kod utan i någon annan utvecklares kod som ingår i samma flöde och då får man avvakta tills dess att de problemen är lösta för att se om allt kan passera igenom CI/CD flödet. 

Om det inte uppstår några problem med testerna skall applikationen "byggas" och det kan ju ske på olika sätt, i Python "byggs" ingen del av koden medans till exempel GoLang så bygger man genom "go build".  
Oftast nu för tiden bygger man containrar av olika slag med applikationen i sig. Om applikationen skulle vara en Flask-app så är det inte mycket som behövs göras förutom att kopieara över Python filerna. Men om applikationen är en GoLang-app skulle applikationen efter test byggas via 'go build' därefter att de nya binära filen/erna har skapats läggas in i en "scratch" container (väldigt naken container) som användas för deployment.

```
Flödet från utvecklaren till Deployment

    + Lokal dator / repository -+                 + Remote repository -+
    | Applikation               --- 'git push' ---> Applikation        |   + CI/CD flöde -------------------------------------+
    +---|------------------^----+                 | med CI/CD flöde    ----> 1. Bygger applikationen med dess "dependencies"  |
        |                  |                      +--------------------+   | 2. Kör definierade tester                        |
        +-- 'git commit' --+                                               | 3. Deployment av applikationen                   |
                                                                           +--------------------------------------------------+

Olika sätt (förenklat) att testa och "bygga" applikationer i containrar beroende på programspråk
 
         Flask-app (python)                                       GoLang-app
        ========================                                 ========================   
         1. Python container med applikationen (koden)            1. Golang container med applikationen (kod)
         2. Kör tester                                            2. Lägg på dependencies
         3. Installera en "server suite" för att få               3. Kör tester
            en "basic server" för Flask                           4. Bygg applikationen (kod -> binärt)
         4. Deployment                                            5. Flytta de binära filerna till en "scratch" container
                                                                  6. Bygg "scratch" container
                                                                  7. Deployment
```

Dock är det värt att nämna att efter att en container har byggs med den nya versionen av applikationen att den mellanlandar i en container repository. Det är sedan härifrån som en eventuell deployment (tets eller poduktion) hämtar den nya containern med applikationen och uppdaterar befintliga containrar med applikationen (äldre versionen) via någon av de olika deployment strategierna som finns.

Den förändring som skett med automatiserad testning har hjälpt utvecklarna genom att det blivit mer eller mindre en standard har det gjort att mer och mer verktyg och tjänster har tagits fram som en utvecklare kan utnyttja. Genom att använda automatiserade tester så blir testningen en del av utvecklingen från början och inte bara en del i slutet. Detta gör att kvalitén på testningen blir högre speciellt om den finns online (tillsammans med koden) som andra utvecklare kan ta del av. Andra fördelar med automatiserade tester eftersom de körs ofta är att fel mellan olika utvecklare och dess kod snabbare kan upptäckas och lösas. En nackdel kan vara om fel uppstår så kommer det också att uppstå för andra utvecklare vid samarbeten, CI/CD flödet kommer inte bli komplett förrän allt har gått genom testningen. Andra nackdelar är att själva CI/CD flödet och dess konfiguration kan ligga utanför utvecklarens ansvarsområde eller kompetens och då är man tvungen att avvakta tills någon annan gjort det man önskat.

Om jag skulle införa ett CI/CD-flöde så skulle jag inte börja med det på dag 1, utan jag skulle börja först ta fram en "bas" och unit tester till den. Därefter när koden kommit lite längre och det är möjligt att bygga en lokala container med applikationen som fungerar på det mest grundläggande sätt (ex: webbsidan/api fungerar vid en Flask-app) då skulle jag se över CI/CD flödet eftersom nu kan något produceras som någon kan användas. Kunskapen finns nu också hur applikationen kan (eller skall) automatiskt testas och byggas som en container, detta gör att det blir lättare att flytta över det till ett CI/CD-flöde.



