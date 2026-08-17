import server


def test_chargement_club():
    # Charge la liste des clubs depuis le fichier JSON
    liste_clubs = server.loadClubs()

    # Vérifie que l'adresse e-mail correspond à un club existant
    resultat = server.verifier_club_existant(
        "john@simplylift.co",
        liste_clubs,
    )

    # Vérifie que le club a bien été trouvé
    assert resultat is True
