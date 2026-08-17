# GÜDLFT Registration

Application web Flask permettant de gérer les réservations de compétitions pour des clubs sportifs.

**Réalisé par Marion Larue** **Début du projet : juillet 2026**

---

## Présentation

GÜDLFT Registration est une application web développée avec Flask dans le cadre du projet OpenClassrooms :

**« Améliorez une application Web Python par des tests et du débogage »**

L'application permet aux secrétaires de clubs de se connecter, de consulter les compétitions disponibles et de réserver des places en utilisant les points de leur club.

Le projet comprend plusieurs niveaux de tests automatisés : tests unitaires, tests d'intégration, tests fonctionnels et tests de performance.

---

## Technologies utilisées

* Python 3.11
* Flask
* JSON
* Pytest
* pytest-cov
* Selenium
* Locust
* Black
* Flake8

---

## Structure du projet

```
Python_Testing/
│
├── templates/
│   ├── booking.html
│   ├── index.html
│   ├── points_clubs.html
│   └── welcome.html
│
├── tests/
│   ├── functional/
│   │   ├── test_parcours_deconnexion.py
│   │   └── test_parcours_reservation_valide.py
│   │
│   ├── integration/
│   │   ├── test_affichage_public_points.py
│   │   ├── test_login.py
│   │   ├── test_points_reservation.py
│   │   ├── test_refus_plus_de_douze_participants.py
│   │   ├── test_refus_reservation_places_indisponibles.py
│   │   ├── test_refus_reservation_points_insuffisants.py
│   │   └── test_server.py
│   │
│   ├── locust/
│   │   ├── locust_points.py
│   │   └── locustfile.py
│   │
│   └── unit/
│       ├── test_unitaire_chargement_clubs.py
│       ├── test_unitaire_chargement_competitions.py
│       ├── test_unitaire_deduction_places.py
│       ├── test_unitaire_deduction_points.py
│       ├── test_unitaire_douze_places.py
│       ├── test_unitaire_places_exactes.py
│       ├── test_unitaire_places_insuffisantes.py
│       ├── test_unitaire_plus_de_douze.py
│       ├── test_unitaire_points_exacts.py
│       └── test_unitaire_points_insuffisants.py
│
├── .flake8
├── .gitignore
├── clubs.json
├── competitions.json
├── pyproject.toml
├── rapport_performances.md
├── rapport_tests.md
├── README.md
├── requirements.txt
└── server.py
```

---

## Installation

### 1. Cloner le dépôt

Clonez le dépôt Git puis placez-vous dans le dossier du projet.

### 2. Créer l'environnement virtuel

```
python -m venv .venv
```

### 3. Activer l'environnement virtuel

Sous Windows PowerShell :

```
.\.venv\Scripts\Activate.ps1
```

Sous macOS ou Linux :

```
source .venv/bin/activate
```

### 4. Installer les dépendances

```
python -m pip install -r requirements.txt
```

---

## Lancer l'application

```
python -m flask --app server run
```

L'application est disponible à l'adresse :

```
http://127.0.0.1:5000
```

---

## Gestion des données

L'application utilise deux fichiers JSON :

* `clubs.json` contient les noms, les adresses e-mail et les points des clubs
* `competitions.json` contient les noms, les dates et les places disponibles

Les données sont chargées au démarrage du serveur. Les réservations modifient les points et les places uniquement en mémoire. Un redémarrage du serveur recharge les données d'origine.

---

## Tests automatisés

La suite automatisée contient 20 tests :

* Tests unitaires : 10
* Tests d'intégration : 8
* Tests fonctionnels : 2

### Tests unitaires

Les tests unitaires vérifient le chargement des données JSON, les règles de réservation et les calculs des points et des places.

```
python -m pytest tests/unit -v
```

### Tests d'intégration

Les tests d'intégration vérifient les routes Flask, les réservations, les cas de refus, l'affichage public des points et le parcours global de l'application.

```
python -m pytest tests/integration -v
```

### Tests fonctionnels

Les tests fonctionnels utilisent Selenium avec un navigateur Chrome. Le serveur Flask doit être lancé avant leur exécution.

```
python -m pytest tests/functional -v
```

### Suite complète

Le serveur Flask doit être actif pour les tests Selenium.

```
python -m pytest -v
```

### Couverture du code

```
python -m pytest --cov=server --cov-report=term-missing -v
```

Résultat obtenu pour `server.py` :

* Instructions mesurées : 78
* Instructions non couvertes : 0
* Couverture obtenue : 100 %
* Couverture minimale demandée : 60 %

---

## Tests de performance

Les tests de performance sont réalisés avec Locust et 6 utilisateurs simulés.

```
python -m locust -f tests/locust/locustfile.py
python -m locust -f tests/locust/locust_points.py
```

Les deux exigences du cahier des charges sont respectées :

* Affichage des compétitions en moins de 5 secondes
* Mise à jour des points en moins de 2 secondes

Les résultats détaillés sont disponibles dans `rapport_performances.md`.

---

## Qualité du code

Black et Flake8 ont été ajoutés pour vérifier le formatage et la qualité du code Python.

```
black .
flake8 .
```

---

## Page publique des points

La page publique affiche en lecture seule les points disponibles de chaque club. Elle est accessible sans connexion depuis la page d'accueil ou directement à l'adresse :

```
http://127.0.0.1:5000/points-clubs
```

---

## Auteur

**Marion Larue**

Projet réalisé dans le cadre de la formation **Développeur d'application Python – OpenClassrooms**.