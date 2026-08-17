import server


def test_chargement_competition():
    # Chargement des compèts depuis Json
    liste_competitions = server.loadCompetitions()

    # Vérification dans la liste
    resultat = server.verifier_competition_existante(
        "Spring Festival",
        liste_competitions,
    )

    assert resultat is True
