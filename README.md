# OLIOT JA TIETOKANNAT

Tämä README kokoaa yhteen kouluprojektini jotka liittyvät olioihin, tietokantoihin ja ohjelmallisiin malleihin. W kansioista löytyy palautettavat tehtäväni (esim. W0, W1 jne..)

---

## Sisältö

### 1. Luokat sekä tyypittäminen
- Luokkien määrittely ja olioiden luonti
- Tietotyypit: int, string, bool, List<T>, DateTime jne.
- Strong typing ja tyypin turvallisuus

### 2. Tietoluokat vs käytösluokat
- **Tietoluokat (Data Classes)**: tallentavat tietoja, sisältävät pääosin kenttiä ja propertyjä
- **Käytösluokat (Service / Logic Classes)**: sisältävät toiminnallisuutta, logiikkaa ja metodeja, jotka käyttävät tietoluokkia

### 3. Olion tila ja serialisointi
- Olion sisäinen tila ja sen hallinta
- Serialisointi: muuntaminen tallennettavaksi tai siirrettäväksi muodoksi (JSON, XML, Binary)
- Deserialisointi: olion palauttaminen tallennetusta muodosta

### 4. Tietokannat ja strukturoitu kyselykieli (SQL)
- Relaatiotietokannat, taulut, sarakkeet ja rivit
- SQL-peruskyselyt: SELECT, INSERT, UPDATE, DELETE
- Ehtolauseet WHERE, ORDER BY, GROUP BY
- Liitokset (JOIN) eri taulujen yhdistämiseen

### 5. Tietokantojen hyödyntäminen ohjelmallisesti
- ADO.NET, Entity Framework tai Dapper
- Yhteyden muodostaminen tietokantaan
- Tietojen hakeminen ja muokkaaminen ohjelman kautta

### 6. Relaatiot ja liitoskyselyt
- Yksi-moneen (1:N), monta-moneen (M:N) relaatiot
- JOIN-kyselyiden hyödyntäminen tiedon yhdistämisessä useista tauluista

### 7. Olio-ohjelmien neljä perus pilaria
- **Abstraktio**: olennaisten ominaisuuksien erottaminen
- **Kapselointi**: tiedon suojaaminen ja metodien kautta hallinta
- **Perintö (Inheritance)**: luokkien uudelleenkäyttö ja hierarkia
- **Polymorfismi**: eri toteutusten käsittely yhtenäisen rajapinnan kautta

### 8. Luokkakaaviot ja tietomallit
- UML-luokkakaaviot
- Tietokantakaaviot (ER-diagrammit)
- Mallien suunnittelu ja dokumentointi

### 9. Kolmannen osapuolen kirjastot
- NuGet-paketit
- Lisäkirjastojen hyödyntäminen projektissa
- Esim. JSON-serialisointi, HTTP-kutsut, tietokantakirjastot

### 10. Extra - Komentoriviargumentit
- Ohjelman syötteiden vastaanotto komentoriviltä
- Argumenttien käsittely ja validointi

### 11. Extra - Säikeistys ja asynkroonisuus
- Monisäikeisyys ja taustatehtävät
- async / await ja tehtävien (Task) hallinta
- Parantaa sovelluksen suorituskykyä ja responsiivisuutta
