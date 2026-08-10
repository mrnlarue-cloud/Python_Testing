# Rapport de performances — GÜDLFT Registration

## Objectif

Les tests de performance ont été réalisés avec Locust afin de vérifier que l'application respecte les exigences définies dans le cahier des charges.

Les tests ont été exécutés en local avec 6 utilisateurs simulés.

Host utilisé :

http://127.0.0.1:5000

## Test 1 — Affichage de la liste des compétitions

Route testée :

POST /showSummary

Cette route permet d'afficher la page contenant la liste des compétitions après la connexion d'un club.

### Exigence

Le temps de réponse doit être inférieur à 5 secondes.

### Résultats

- Utilisateurs simulés : 6
- Requêtes : 311
- Échecs : 0
- Temps moyen : 5,21 ms
- Médiane : 5 ms
- Minimum : 3 ms
- Maximum : 22 ms
- 95e percentile : 8 ms
- 99e percentile : 13 ms
- Débit : Environ 24,3 requêtes par seconde

### Conclusion

**Exigence respectée**

Le temps de réponse maximum observé est de 22 ms, très inférieur à la limite de 5 secondes définie dans le cahier des charges.

## Test 2 — Mise à jour des points

Route testée :

POST /purchasePlaces

Cette route effectue une réservation et met à jour les points du club ainsi que le nombre de places disponibles pour la compétition.

### Exigence

La mise à jour des points doit être effectuée en moins de 2 secondes.

### Résultats

- Utilisateurs simulés : 6
- Requêtes : 6
- Échecs : 0
- Temps moyen : 5,95 ms
- Médiane : 4 ms
- Minimum : 3 ms
- Maximum : 15 ms
- 95e percentile : 15 ms
- 99e percentile : 15 ms

### Conclusion

**Exigence respectée**

Le temps de réponse maximum observé est de 15 ms, très inférieur à la limite de 2 secondes définie dans le cahier des charges.

## Difficultés rencontrées

Lors du premier scénario de charge, l'absence de délai entre les requêtes provoquait un nombre très important de connexions et a entraîné une erreur WinError 10048 sous Windows.

Le scénario Locust a donc été ajusté afin de représenter une charge adaptée aux exigences du projet sans modifier l'application Flask.

Pour le test de mise à jour des points, les réservations modifient les données chargées en mémoire par Flask. Le scénario final a donc été conçu afin d'éviter que les utilisateurs simulés n'épuisent artificiellement les points disponibles pendant la mesure.

## Conclusion générale

Les deux scénarios respectent les objectifs de performance définis dans le cahier des charges :

- Affichage de la liste des compétitions : **Exigence respectée**
- Mise à jour des points après une réservation : **Exigence respectée**

Les temps de réponse observés sont très inférieurs aux limites imposées et aucun échec HTTP n'a été observé pendant les scénarios finaux.