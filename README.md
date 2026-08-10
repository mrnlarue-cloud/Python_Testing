# GÜDLFT Registration

Application web Flask permettant de gérer les réservations de compétitions pour des clubs sportifs.

**Réalisé par Marion Larue**
**Début du projet : juillet 2026**

---

## Présentation

GÜDLFT Registration est une application web développée avec Flask dans le cadre du projet OpenClassrooms :

**« Améliorez une application Web Python par des tests et du débogage »**

L'application permet aux secrétaires de clubs sportifs de se connecter, de consulter les compétitions disponibles et de réserver des places en utilisant les points de leur club.

Le projet comprend plusieurs niveaux de tests automatisés permettant de vérifier :

* Les règles métier ;
* Les routes Flask ;
* Les interactions entre les différentes parties de l'application ;
* Les parcours utilisateurs complets ;
* Les performances de l'application.

---

## Fonctionnalités

* Connexion d'un club à l'aide d'une adresse e-mail ;
* Affichage des compétitions disponibles ;
* Réservation de places pour une compétition ;
* Limite de 12 places maximum par réservation ;
* Vérification des points disponibles du club ;
* Vérification des places disponibles pour la compétition ;
* Déduction automatique des points après une réservation valide ;
* Déduction automatique des places disponibles après une réservation valide ;
* Page publique affichant les points de tous les clubs ;
* Déconnexion.

---

## Technologies utilisées

* Python 3.11 ;
* Flask ;
* JSON ;
* Pytest ;
* pytest-cov ;
* Selenium ;
* Locust ;
* Black ;
* Flake8.

---

## Structure du projet

```text
Python_Testing/
│
├── .venv/
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
│   │   └── test_refus_reservation_points_insuffisants.py
│   │
│   ├── locust/
│   │   ├── locust_points.py
│   │   └── locustfile.py
│   │
│   └── unit/
│       ├── test_unitaire_deduction_places.py
│       ├── test_unitaire_deduction_points.py
│       ├── test_unitaire_douze_places.py
│       ├── test_unitaire_places_exactes.py
│       ├── test_unitaire_places_insuffisantes.py
│       ├── test_unitaire_plus_de_douze.py
│       ├── test_unitaire_points_exacts.py
│       └── test_unitaire_points_insuffisants.py
│
├── .coverage
├── .flake8
├── .gitignore
├── clubs.json
├── competitions.json
├── pyproject.toml
├── README.md
├── requirements.txt
└── server.py
```

### Principaux fichiers

* `server.py` : Application Flask et logique métier ;
* `clubs.json` : Données des clubs ;
* `competitions.json` : Données des compétitions ;
* `templates/` : Templates HTML de l'application ;
* `tests/unit/` : Tests unitaires ;
* `tests/integration/` : Tests d'intégration ;
* `tests/functional/` : Tests fonctionnels Selenium ;
* `tests/locust/` : Scénarios de tests de performance Locust ;
* `requirements.txt` : Dépendances Python ;
* `pyproject.toml` : Configuration de Black ;
* `.flake8` : Configuration de Flake8.

---

## Installation

### 1. Cloner le dépôt

Clonez le dépôt Git puis placez-vous dans le dossier du projet.

### 2. Créer l'environnement virtuel

```bash
python -m venv .venv
```

### 3. Activer l'environnement virtuel

Sous **Windows PowerShell** :

```powershell
.\.venv\Scripts\Activate.ps1
```

Sous **macOS ou Linux** :

```bash
source .venv/bin/activate
```

### 4. Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

---

## Lancer l'application

Démarrez le serveur de développement Flask :

```bash
python -m flask --app server run
```

L'application est ensuite disponible à l'adresse :

```text
http://127.0.0.1:5000
```

---

## Gestion des données

L'application utilise des fichiers JSON à la place d'une base de données.

### `clubs.json`

Ce fichier contient notamment :

* Le nom des clubs ;
* Leur adresse e-mail ;
* Leur nombre de points disponibles.

### `competitions.json`

Ce fichier contient notamment :

* Le nom des compétitions ;
* Leur date ;
* Leur nombre de places disponibles.

Les fichiers JSON sont chargés lorsque le serveur Flask démarre.

Lorsqu'une réservation est effectuée, les points du club et les places disponibles pour la compétition sont modifiés **en mémoire**.

Ces modifications ne sont pas enregistrées dans les fichiers JSON.

Un redémarrage du serveur Flask recharge donc les données d'origine.

---

## Tests automatisés

Le projet utilise plusieurs niveaux de tests afin de vérifier séparément les règles métier, le fonctionnement des routes et les parcours complets de l'utilisateur.

### Tests unitaires

Les tests unitaires vérifient individuellement les fonctions métier de l'application.

Ils couvrent notamment :

* Le refus d'une réservation supérieure à 12 places ;
* L'acceptation d'une réservation de 12 places exactement ;
* Le refus en cas de points insuffisants ;
* L'acceptation lorsque les points sont exactement suffisants ;
* Le refus lorsque les places disponibles sont insuffisantes ;
* L'acceptation lorsque les places sont exactement suffisantes ;
* Le calcul des points restants ;
* Le calcul des places restantes.

Pour exécuter les tests unitaires :

```bash
python -m pytest tests/unit -v
```

---

### Tests d'intégration

Les tests d'intégration vérifient les interactions entre les routes Flask, les règles métier et les données de l'application.

Ils couvrent notamment :

* La connexion avec une adresse valide ;
* Le refus d'une adresse e-mail inconnue ;
* L'affichage de la page publique des points ;
* Une réservation valide ;
* La mise à jour des points ;
* Le refus d'une réservation supérieure à 12 places ;
* Le refus lorsque les points sont insuffisants ;
* Le refus lorsque les places sont insuffisantes.

Pour exécuter les tests d'intégration :

```bash
python -m pytest tests/integration -v
```

---

### Tests fonctionnels avec Selenium

Les tests fonctionnels utilisent Selenium avec un véritable navigateur Chrome afin de reproduire des parcours utilisateurs complets.

Ils vérifient notamment :

* La connexion ;
* L'accès à une compétition ;
* La réservation d'une place ;
* La mise à jour des points ;
* La déconnexion ;
* Le retour à la page d'accueil.

Le serveur Flask doit être lancé avant d'exécuter ces tests.

Dans un premier terminal :

```bash
python -m flask --app server run
```

Dans un second terminal :

```bash
python -m pytest tests/functional -v
```

---

### Exécuter la suite complète

Le serveur Flask doit être actif pour permettre l'exécution des tests fonctionnels Selenium.

Dans un premier terminal :

```bash
python -m flask --app server run
```

Dans un second terminal :

```bash
python -m pytest -v
```

---

### Couverture des tests

Le projet utilise `pytest-cov` afin de mesurer la proportion du code exécutée pendant les tests.

Commande utilisée :

```bash
python -m pytest --cov=server --cov-report=term-missing -v
```

Le cahier des charges demande une couverture de code minimale de **60 %**.

La couverture obtenue pour `server.py` est de **88 %**.

L'objectif n'est pas d'atteindre artificiellement 100 %, mais de disposer d'une couverture suffisante et pertinente des comportements importants de l'application.

---

## Tests de performance

Les tests de performance sont réalisés avec **Locust**.

Le cahier des charges impose une simulation avec **6 utilisateurs simulés** et les objectifs suivants :

* Affichage de la liste des compétitions en moins de **5 secondes** ;
* Mise à jour des points après une réservation en moins de **2 secondes**.

Le serveur Flask doit être lancé avant Locust :

```bash
python -m flask --app server run
```

### Liste des compétitions

Dans un autre terminal :

```bash
python -m locust -f tests/locust/locustfile.py
```

Ce scénario teste la route :

```text
POST /showSummary
```

### Mise à jour des points

Dans un autre terminal :

```bash
python -m locust -f tests/locust/locust_points.py
```

Ce scénario teste la route :

```text
POST /purchasePlaces
```

### Configuration de Locust

Dans l'interface Locust, utilisez les paramètres suivants :

* Nombre d'utilisateurs : `6` ;
* Taux de démarrage : `1` ;
* Host : `http://127.0.0.1:5000`.

L'interface est accessible à l'adresse :

```text
http://localhost:8089
```

Les deux scénarios respectent les objectifs de performance définis dans le cahier des charges.

---

## Qualité du code

### Black

J'ai ajouté **Black** au projet afin d'utiliser un formatage automatique et homogène du code Python.

Black ne faisait pas partie du projet de départ. Il s'agit d'un ajout personnel réalisé afin d'améliorer la qualité et la cohérence du code.

Pour formater le projet :

```bash
black .
```

La configuration associée se trouve dans :

```text
pyproject.toml
```

### Flake8

J'ai également ajouté **Flake8** afin de vérifier le respect des conventions de style Python et de détecter certains problèmes de qualité du code.

Flake8 ne faisait pas partie du projet de départ. Il s'agit également d'un ajout personnel.

Pour vérifier le projet :

```bash
flake8 .
```

La configuration associée se trouve dans :

```text
.flake8
```

Black et Flake8 sont utilisés ensemble afin de conserver un code lisible, cohérent et facile à maintenir.

---

## Page publique des points

L'application comprend une page publique en lecture seule affichant les points disponibles de chaque club.

Elle est accessible à l'adresse :

```text
http://127.0.0.1:5000/points-clubs
```

Aucune authentification n'est nécessaire pour consulter cette page.

---

## Auteur

**Marion Larue**

Projet réalisé dans le cadre de la formation **Développeur d'application Python – OpenClassrooms**.
