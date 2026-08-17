# =========================
# IMPORTS
# =========================

import json
from flask import Flask, render_template, request, redirect, flash, url_for

# =========================
# CHARGEMENT DES DONNÉES JSON
# =========================


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


# =========================
# VÉRIFICATION DES DONNÉES CHARGÉES
# =========================


def verifier_club_existant(email, liste_clubs):
    # Parcours tous les clubs JSON
    for club in liste_clubs:
        # Retourne True dès que l'adresse e-mail est trouvée
        if club["email"] == email:
            return True

    # Retourne False si aucun club ne correspond
    return False


def verifier_competition_existante(nom_competition, liste_competitions):
    # Parcours toutes les compétitions JSON
    for competition in liste_competitions:
        # Retourne True dès que le nom de la compétition est trouvé
        if competition["name"] == nom_competition:
            return True

    # Retourne False si aucune compétition ne correspond
    return False


# =========================
# CONFIGURATION DE FLASK
# =========================

app = Flask(__name__)
app.secret_key = "something_special"


# =========================
# DONNÉES DE L’APPLICATION
# =========================

competitions = loadCompetitions()
clubs = loadClubs()


# =========================
# PAGE D’ACCUEIL
# =========================


@app.route("/")
def index():
    return render_template("index.html")


# =========================
# CONNEXION D’UN CLUB
# =========================


@app.route("/showSummary", methods=["POST"])
def showSummary():
    email = request.form["email"]

    # Vérifie que l'adresse e-mail correspond à un club existant
    if not verifier_club_existant(email, clubs):
        flash("Désolé, cette adresse e-mail n’a pas été trouvée.")

        # Redirige vers la page d'accueil
        return redirect(url_for("index"))

    # Recherche le club correspondant à l'adresse e-mail
    clubs_trouves = [club for club in clubs if club["email"] == email]
    club = clubs_trouves[0]

    return render_template(
        "welcome.html",
        club=club,
        competitions=competitions,
    )


# =========================
# AFFICHAGE DU FORMULAIRE DE RÉSERVATION
# =========================


@app.route("/book/<competition>/<club>")
def book(competition, club):
    # Vérifie que la compét existe
    if not verifier_competition_existante(competition, competitions):
        flash("Désolé, cette compétition n’a pas été trouvée.")

        # Redirige vers la page d'accueil
        return redirect(url_for("index"))

    # Recherche le club et la compét
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]

    # Affiche la page de résa
    return render_template(
        "booking.html",
        club=foundClub,
        competition=foundCompetition,
    )


# =========================
# VALIDATION D’UNE RÉSERVATION
# =========================


def verifier_limite_places(nombre_places):
    # Max 12 places
    return nombre_places <= 12


def verifier_points_suffisants(points, nombre_places):
    # Vérifie qu'il y a assez de points
    return points >= nombre_places


def verifier_places_disponibles(places_disponibles, nombre_places):
    # Vérifie les places dispos
    return places_disponibles >= nombre_places


def calculer_points_restants(points, nombre_places):
    # Calcule les points restants
    return points - nombre_places


def calculer_places_restantes(places_disponibles, nombre_places):
    # Calcule les places restantes
    return places_disponibles - nombre_places


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    # Recherche d'une compétition
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]

    # Recherche d'un club
    club = [c for c in clubs if c["name"] == request.form["club"]][0]

    placesRequired = int(request.form["places"])

    # Limite de 12 places
    if not verifier_limite_places(placesRequired):
        flash("Vous ne pouvez pas réserver plus de douze places")
        # Affiche la page du club, la compète et la liste des compètes
        return render_template(
            "welcome.html",
            club=club,
            competition=competition,
            competitions=competitions,
        )

    # Points insuffisants
    if not verifier_points_suffisants(int(club["points"]), placesRequired):
        flash("Vous n’avez pas assez de points.")
        return render_template(
            "welcome.html",
            club=club,
            competition=competition,
            competitions=competitions,
        )

    # Places insuffisantes
    if not verifier_places_disponibles(
        int(competition["numberOfPlaces"]), placesRequired
    ):
        flash("Il n’y a pas assez de places disponibles.")
        return render_template(
            "welcome.html",
            club=club,
            competition=competition,
            competitions=competitions,
        )

    # Déduction des places
    competition["numberOfPlaces"] = calculer_places_restantes(
        int(competition["numberOfPlaces"]), placesRequired
    )

    # Déduction des points
    club["points"] = calculer_points_restants(int(club["points"]), placesRequired)

    # Confirmation
    flash("Great-booking complete!")

    return render_template(
        "welcome.html",
        club=club,
        competition=competition,
        competitions=competitions,
    )


# =========================
# AFFICHAGE PUBLIC DES POINTS
# =========================


@app.route("/points-clubs")
def afficher_points_clubs():
    return render_template(
        "points_clubs.html",
        clubs=clubs,
    )


# =========================
# DÉCONNEXION
# =========================


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
