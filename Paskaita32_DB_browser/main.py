'''
Išrinkite visus duomenis iš lentelės “DARBUOTOJAI”.
1. SELECT * FROM DARBUOTOJAI


2.Išrinkite visus duomenis iš stulpelio “GIMIMO_DATA” - lentelėje “DARBUOTOJAI”.
SELECT GIMIMO_DATA FROM DARBUOTOJAI

3.Išrinkite visus duomenis iš stulpelių “VARDAS”,”PAVARDĖ”, “PAREIGOS” - lentelėje “DARBUOTOJAI”
SELECT VARDAS, PAVARDĖ, PAREIGOS FROM DARBUOTOJAI

4.Išrinkite unikalias reikšmes iš stulpelio SKYRIUS_PAVADINIMAS - lentelėje “DARBUOTOJAI”.
SELECT DISTINCT SKYRIUS_PAVADINIMAS FROM DARBUOTOJAI

5.Išrinkite visus duomenis apie darbuotojus, kurie dirba Gamybos skyriuje.
SELECT * FROM DARBUOTOJAI WHERE SKYRIUS_PAVADINIMAS="Gamybos"

6.Išrinkite duomenis, kokias pareigas užima Giedrius
SELECT * FROM DARBUOTOJAI WHERE VARDAS="Giedrius"

7.Išrinkite visus duomenis apie darbuotojus, kurių gimimo data - 1986-09-19
SELECT * FROM DARBUOTOJAI WHERE GIMIMO_DATA="1986-09-19"

8.Išrinkite darbuotojų vardus, kurių pavardės yra Sabutis
SELECT VARDAS FROM DARBUOTOJAI WHERE PAVARDĖ="Sabutis"

9.Išrinkite duomenis (vardą ir pavardę) apie programuotojus iš Gamybos skyriaus
SELECT VARDAS, PAVARDĖ FROM DARBUOTOJAI WHERE SKYRIUS_PAVADINIMAS="Gamybos" AND PAREIGOS="Programuotojas"

10.Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami visus reikiamus laukus
(vardą, pavardę, gimimo metus, pareigas, skyriaus pavadinimą).
INSERT INTO DARBUOTOJAI VALUES("Edvinas", "Juodeika", "2000-07-28", "Programuotojas", "Gamybos")

11.Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami tik laukus
(vardą, pavardę, gimimo metus). Pareigas ir skyriaus pavadinimą palikite neužpildytus.
INSERT INTO DARBUOTOJAI(VARDAS, PAVARDĖ, GIMIMO_DATA) VALUES("Paulius", "Jankunas", "1984-04-29")

12.Užpildykite likusius tuščius laukus “DARBUOTOJAI” lentelėje, jūsų prieš tai įterptame įraše.
Priskirkite darbuotojui pareigas ir skyrių.
UPDATE DARBUOTOJAI SET PAREIGOS = "Vadybininkas" , SKYRIUS_PAVADINIMAS = "Pardavimų" WHERE PAVARDĖ = "Jankunas"

13.Ištrinkite lentelės “DARBUOTOJAI” įrašą, kurio gimimo data yra tokia, kurią jūs sukūrėte.
DELETE FROM DARBUOTOJAI WHERE GIMIMO_DATA = "2000-07-28"

14.Įterpkite, du darbuotojus, pavarde Antanaitis kurių pareigos būtų “Programuotojas”.
INSERT INTO DARBUOTOJAI
VALUES
  ("Jonas", "Antanaitis", "1997-10-15", "Programuotojas", "Gamybos"),
  ("Algirdas", "Antanaitis", "1989-12-24", "Programuotojas", "Gamybos");

15.Pakeiskite, abiejų Antanaičių pareigas į “Testuotojas” vienu sakiniu.
UPDATE DARBUOTOJAI
SET PAREIGOS = "Testuotojas"
WHERE (PAVARDĖ = "Antanaitis" AND VARDAS = "Jonas")
OR (PAVARDĖ = "Antanaitis" AND VARDAS = "Algirdas")

16.Suskaičiuokite, kiek įmonėje dirba Testuotojų.
SELECT SUM(PAREIGOS = "Testuotojas") FROM DARBUOTOJAI
'''