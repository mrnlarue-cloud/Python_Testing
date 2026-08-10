# Rapport des tests, Projet GÜDLFT Registration

## Outils utilisés

Pour réaliser les tests de l'application, j'ai principalement utilisé :

- Pytest pour les tests unitaires et les tests d'intégration
- Selenium pour les tests fonctionnels dans un navigateur
- pytest-cov pour mesurer la couverture du code

## Mes résultats

La suite de tests automatisés contient ici 17 tests :

- Tests unitaires : 8
- Tests d'intégration 7
- Tests fonctionnels : 2

Pour la validation finale :

- Tests réussis : 17
- Tests échoués : 0

Command à utiliser :

`python -m pytest -v`

## Couverture du code

La couverture est mesurée avec `pytest-cov` :

`python -m pytest --cov=server --cov-report=term-missing -v`

Les résultats obtenus :

- `server.py` : 88 % de couverture
- Couverture minimale demandée : 60 %
- Instructions mesurées : 66
- Instructions non couvertes : 8
- Lignes non couvertes : 48, 79-92 et 208

**Exigence de couverture respectée.**

## Conclusion

Les 17 tests automatisés sont réussis et la couverture de `server.py` atteint 88 %, contre un minimum spécifié de 60 %.

Les tests couvrent les règles métier, les interactions entre les routes Flask et les parcours utilisateurs principaux de l'application.

La couverture n'atteint pas 100 % car certaines lignes et certains chemins secondaires de l'application ne sont pas exécutés par la suite de tests actuelle. 
Mon objectif a été de privilégier des tests pertinents sur les comportements importants et les principaux cas d'erreurs plutôt que d'ajouter des tests uniquement pour augmenter le pourcentage de couverture.
Je précise ici qu'un taux de couverture de 100 % ne garantirait par ailleurs pas l'absence totale de bugs : la couverture indique principalement quelles parties du code ont été exécutées pendant les tests.

**Les exigences de test et de couverture du projet sont respectées.**
