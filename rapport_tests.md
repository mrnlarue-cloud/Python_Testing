# Rapport des tests, Projet GÜDLFT Registration

## Outils utilisés

Pour réaliser les tests de l'application, j'ai principalement utilisé :

* Pytest pour les tests unitaires et les tests d'intégration
* Selenium pour les tests fonctionnels dans un navigateur
* pytest-cov pour mesurer la couverture du code

## Mes résultats

La suite de tests automatisés contient 20 tests :

* Tests unitaires : 10
* Tests d'intégration : 8
* Tests fonctionnels : 2

Pour la validation finale :

* Tests réussis : 20
* Tests échoués : 0

Commande à utiliser :

`python -m pytest -v`

## Couverture du code

La couverture est mesurée avec `pytest-cov` :

`python -m pytest --cov=server --cov-report=term-missing -v`

Les résultats obtenus :

* `server.py` : 100 % de couverture
* Couverture minimale demandée : 60 %
* Instructions mesurées : 78
* Instructions non couvertes : 0
* Lignes non couvertes : aucune

**Exigence de couverture respectée.**

## Conclusion

Les 20 tests automatisés sont réussis et la couverture de `server.py` atteint 100 %, contre un minimum spécifié de 60 %.

Les tests couvrent les règles métier, les interactions entre les routes Flask et les parcours utilisateurs principaux de l'application.

Un taux de couverture de 100 % ne garantit pas l'absence totale de bugs, mais confirme que toutes les instructions de `server.py` ont été exécutées pendant les tests.

**Les exigences de test et de couverture du projet sont respectées.**
