<h1>Schrijven een github action</h1>

Voor dit deel van de cursus was het nodig om op ubuntu te werken. Dat vormde voor mij de eerste moeilijkheid. Inmiddels heb ik mij zelf dat meer eigen gemaakt. Als tweede stap vond ik het lastig om de opdracht echt goed te begrijpen. Het duurde een tijdje voordat ik goed door had dat het uiteindelijk om een automatische deploy van de software naar ubuntu te maken. Uiteindelijk is het wel gelukt, maar ik heb er best even over gedaan. De belangrijkste componenten uit mijn action betreffen :
-  Het runnen van een eenvoudig testscript  
-  Het uitvoeren van een scp kopieeractie 
-  Het uitvoeren van aantal remote commando's op basis van een ssh

Ik vind dat er uiteindelijk vrij veel op internet moest worden opgezocht om uit te vinden hoe de verschillende stappen ten uitvoer konden worden gebracht. 

<h1>uitvoer van het testscript</h1>

Het was mij in eerste instantie niet helder hoe ik een testscript kan uitvoeren voor een eenvoudige flask app. Ik vond in eerste instantie wel testscripts voor functies in een main py maar daarbij werden de functies met een antwoord "geassert". Nu lijkt een flask app daar wel enigszins op maar het is het toch niet helemaal. Dat komt doordat je met een flask app een verbinding met localhost:5000 bewerkstelligt. Daarom moet je je realiseren dat je als je een flask app test de client verbinding aan het testen bent. Als je de app aan het testen bent, wil je derhalve in eerste instantie een response code 200 terug krijgen om te verifieren dat de verbinding succesvol is. 
Daarnaast kun je dan met een assert op response.data eenvoudige functies controleren. 

<h1>Bruggetje tussen testscript en scp/ssh action</h1>

Het bruggetje dat ik tussen het testscript en de scp en ssh actions heb toegepast is een controle op de functie success(). De functies uit het testscript worden op basis van iedere push actie uitgevoerd. Daarvoor wordt op basis van de requirements file python en flask gebruikt. Binnen github wordt van environment variables gebruik gemaakt waarvan de functie ${{success()}} gebruik maakt. Als het testscript niet succesvol heeft gedraaid dan retourneert de functie success false. Het is alleen true als dat wel lukt. Op basis hiervan kun je bij de daarop volgende scp en ssh acties dus eenvoudig weg stellen dat deze alleen in het geval van true uitgevoerd hoeven te worden. 

<h1>Instellen van een SSH-key</h1>

In eerste instantie heb ik een productie server verbinding aan mijn directory onder ubuntu toegevoegd. Op basis hiervan kan ook een installatie naar ubuntu worden uitgevoerd. Daarna heb ik mij pas gerealiseerd en op internet gevonden dat je een automatische deploy vanuit een action uit kunt voeren. Ik heb op dat moment met ssh-keygen wel een SSH private en public key kunnen maken, maar dit heb ik op basis van secrets nooit kunnen activeren. De melding die ik bleef krijgen was dat er geen SSH key werd gevonden. Om de opdracht succesvol uit te kunnen voeren ben ik maar op basis van een paswoord verder gegaan. Dat werkte wel meteen op basis van secrets.

<h1>SCP actie</h1>

Bij de uitvoer van de SCP actie was het probleem in het niet kunnen activeren van de SSH-key gelegen. Dit probleem heb ik omzeild door van password gebruik te maken. 

<h1>Logging<h1>

Ik heb het loggen gedaan door van remote commands gebruik te maken. Dat is een ssh-action dat van script gebruik maakt. Er vallen meerdere commando's achter elkaar uit te voeren door in het script commando een pipe op te nemen. 

