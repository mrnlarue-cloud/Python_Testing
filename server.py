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
    clubs_trouves = [club for club in clubs if club["email"] == request.form["email"]]

    if not clubs_trouves:
        return "Désolé, cette adresse e-mail n’a pas été trouvée."

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
    foundClub = [c for c in clubs if c["name"] == club][0]

    foundCompetition = [c for c in competitions if c["name"] == competition][0]

    if foundClub and foundCompetition:
        return render_template(
            "booking.html",
            club=foundClub,
            competition=foundCompetition,
        )
    else:
        flash("Something went wrong-please try again")

        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
        )


# =========================
# VALIDATION D’UNE RÉSERVATION
# =========================


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    # Recherche de la compétition choisie
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]

    # Recherche du club qui réserve
    club = [c for c in clubs if c["name"] == request.form["club"]][0]

    placesRequired = int(request.form["places"])

    # Refus si le club demande plus de 12 places
    if placesRequired > 12:
        flash("Vous ne pouvez pas réserver plus de douze places")
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
        )

    # Refus si le club ne possède pas assez de points
    if placesRequired > int(club["points"]):
        flash("Vous n’avez pas assez de points.")
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
        )

    # Déduction des places réservées
    competition["numberOfPlaces"] = int(competition["numberOfPlaces"]) - placesRequired

    # Déduction des points utilisés par le club
    club["points"] = int(club["points"]) - placesRequired

    # Confirmation de la réservation
    flash("Great-booking complete!")

    # Retour sur la page récapitulative du club
    return render_template(
        "welcome.html",
        club=club,
        competitions=competitions,
    )


# =========================
# AFFICHAGE PUBLIC DES POINTS
# FONCTIONNALITÉ À DÉVELOPPER EN PHASE 2
# =========================

# TODO: Add route for points display


# =========================
# DÉCONNEXION
# =========================


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
