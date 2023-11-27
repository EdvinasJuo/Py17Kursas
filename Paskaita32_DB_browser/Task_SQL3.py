"""
1. Išrinkite darbuotojų vardus ir pavardes kartu su projekto pavadinimu, kuriame jie dirba.

SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDĖ, PROJEKTAS.PAVADINIMAS
FROM DARBUOTOJAS
JOIN PROJEKTAS
ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
------------------------------------------------------------------------------------------------
2. Išsirinkite darbuotojų dirbančių projekte Galerija vardus, pavardes ir projekto pavadinimą.

SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDĖ, PROJEKTAS.PAVADINIMAS
FROM DARBUOTOJAS
JOIN PROJEKTAS
ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PROJEKTAS.ID = 1

------------------------------------------------------------------------------------------------
3. Išrinkite visus projekto Projektų valdymas vykdytojus dirbančius Pardavimų skyriuje.

SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDĖ, PROJEKTAS.PAVADINIMAS
FROM DARBUOTOJAS
JOIN PROJEKTAS
ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PROJEKTAS.ID = 2 AND SKYRIUS_ID = 3

------------------------------------------------------------------------------------------------
4. Išrinkite visas moteris, dirbančias projekte Projektų valdymas
ir išveskite į ekraną jų vardus, pavardes ir projekto pavadinimą.

SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDĖ, PROJEKTAS.PAVADINIMAS
FROM DARBUOTOJAS
JOIN PROJEKTAS
ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PROJEKTAS.ID = 2
AND (DARBUOTOJAS.ASMENS_KODAS LIKE '2%' OR DARBUOTOJAS.ASMENS_KODAS LIKE '4%' OR DARBUOTOJAS.ASMENS_KODAS LIKE '6%')

------------------------------------------------------------------------------------------------
5. Išrinkite skyrių pavadinimus su juose dirbančių darbuotojų skaičiumi.

SELECT SKYRIUS.PAVADINIMAS, count(DARBUOTOJAS.ID) AS "Darbuotojų skaičius"
FROM SKYRIUS
JOIN DARBUOTOJAS ON SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID
GROUP BY SKYRIUS.PAVADINIMAS

------------------------------------------------------------------------------------------------
6. Apribokite #5 užklausos rezultatą taip, kad rodytų tik tuos skyrius kur dirba bent 5 darbuotojai.

SELECT SKYRIUS.PAVADINIMAS, count(DARBUOTOJAS.ID) AS "Darbuotojų skaičius"
FROM SKYRIUS
JOIN DARBUOTOJAS ON SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID
GROUP BY SKYRIUS.PAVADINIMAS
HAVING count() > 5

------------------------------------------------------------------------------------------------
7. Išrinkite darbuotojus (vardus, pavardes, pareigas) kartu su skyrių, kuriuose jie dirba pavadinimais, tačiau nesančius tų skyrių vadovais.

SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDĖ, DARBUOTOJAS.PAREIGOS
FROM DARBUOTOJAS
JOIN SKYRIUS ON SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID
WHERE DARBUOTOJAS.PAREIGOS != "Vadovas"

------------------------------------------------------------------------------------------------
8. Sukurkite naują įrašą lentelėje “DARBUOTOJAS”
(asmens kodas: 38807117896, vardas: Pranas, pavardė:Logis, Dirba nuo: 2009-11-12, visa kita - Null).

INSERT INTO DARBUOTOJAS (VARDAS, PAVARDĖ, ASMENS_KODAS, DIRBA_NUO)
VALUES ("Pranas", "Logis", "38807117896", "2009-11-12")
------------------------------------------------------------------------------------------------
9. Išrinkite darbuotojų vardus, pavardes ir skyriaus pavadinimą.
Rodykite, net ir tuos darbuotojus, kurie nedirba jokiame skyriuje (skyriaus pavadinimą pasiimkite iš lentelės SKYRIUS).

SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDĖ, SKYRIUS.PAVADINIMAS
FROM DARBUOTOJAS
LEFT JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID


------------------------------------------------------------------------------------------------
10. 1# punkto užklausą pataisykite taip, kad rodytų tik tuos vardus
ir projektų pavadinimus kuriuose dirba daugiau nei 4 darbuotojai.

SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDĖ, PROJEKTAS.PAVADINIMAS
FROM DARBUOTOJAS
JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
WHERE PROJEKTAS.ID IN

(SELECT SKYRIUS_ID
FROM DARBUOTOJAS
GROUP BY SKYRIUS_ID
HAVING COUNT() > 4)
ORDER BY PAVADINIMAS

------------------------------------------------------------------------------------------------
11. Naujame stulpeyje parodyti kiekvieno darbuotojo bazinio atlyginimo ir priedų sumą.

SELECT VARDAS, PAVARDĖ, BAZINIS_ATLYGINIMAS, PRIEDAI,(BAZINIS_ATLYGINIMAS + PRIEDAI) AS Alga_su_priedu
FROM DARBUOTOJAS

------------------------------------------------------------------------------------------------
12. Parodyti bendrą atlyginimų, priedų sumą, vidutinį, maksimalų, minimalų atlyginimą.

SELECT sum(BAZINIS_ATLYGINIMAS) as Bendras_Atlyginimas,
sum(PRIEDAI) as Bendra_priedu_suma,
ROUND(AVG(BAZINIS_ATLYGINIMAS), 2) as Vidutinis_atlyginimas,
max(BAZINIS_ATLYGINIMAS) as Maksimalus_atlyginimas,
min(BAZINIS_ATLYGINIMAS) as Minimalus_atlyginimas
FROM DARBUOTOJAS
------------------------------------------------------------------------------------------------
"""