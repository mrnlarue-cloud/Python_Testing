# Rapport de performances — Projet GÜDLFT Registration

## Mes tests de performance

J'ai utilisé Locust pour vérifier les deux exigences de performance demandées dans le projet.

Les tests ont été réalisés en local avec 6 utilisateurs simulés.

Host utilisé :

`http://127.0.0.1:5000`

## Affichage de la liste des compétitions

Route testée :

`POST /showSummary`

L'affichage de la liste des compétitions doit prendre moins de 5 secondes.

Mes résultats :

- Requêtes : 311
- Échecs : 0
- Temps moyen : 5,21 ms
- Médiane : 5 ms
- Minimum : 3 ms
- Maximum : 22 ms
- 95e percentile : 8 ms
- 99e percentile : 13 ms

Le temps maximum observé est de 22 ms, pour une limite de 5 secondes.

**Exigence respectée.**

## Mise à jour des points

Route testée :

`POST /purchasePlaces`

La mise à jour des points doit prendre moins de 2 secondes.

Mes résultats :

- Requêtes : 6
- Échecs : 0
- Temps moyen : 5,95 ms
- Médiane : 4 ms
- Minimum : 3 ms
- Maximum : 15 ms
- 95e percentile : 15 ms
- 99e percentile : 15 ms

Le temps maximum observé est de 15 ms, pour une limite de 2 secondes.

**Exigence respectée.**

## Difficulté rencontrée

Lors de mon premier test, Locust envoyait beaucoup trop de requêtes sans temps d'attente et j'ai rencontré une erreur `WinError 10048` sous Windows.
J'ai donc corrigé le scénario Locust en ajoutant un temps d'attente adapté.

Pour le test de mise à jour des points, j'ai également limité le nombre de réservations car les données sont modifiées en mémoire pendant l'exécution de l'application.

## Conclusion

Les deux exigences de performance demandées sont respectées :

- Affichage de la liste des compétitions en moins de 5 secondes : **Exigence respectée**
- Mise à jour des points en moins de 2 secondes : **Exigence respectée**

Les résultats obtenus sont donc inférieurs aux limites demandées.