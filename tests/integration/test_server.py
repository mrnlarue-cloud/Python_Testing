import server


def test_parcours_complet_serveur(monkeypatch):
    # Données de test
    clubs_tests = [
        {
            "name": "ClubTest",
            "email": "club@test.com",
            "points": "13",
        }
    ]

    competitions_tests = [
        {
            "name": "CompetitionTest",
            "date": "2026-08-17 10:00:00",
            "numberOfPlaces": "25",
        }
    ]

    # Remplacement avec fausses données
    monkeypatch.setattr(server, "clubs", clubs_tests)
    monkeypatch.setattr(server, "competitions", competitions_tests)

    client_test = server.app.test_client()

    # Accueil
    reponse = client_test.get("/")

    assert reponse.status_code == 200

    # Connexion
    reponse = client_test.post(
        "/showSummary",
        data={"email": "club@test.com"},
    )

    assert "club@test.com" in reponse.get_data(as_text=True)

    # Compétition inconnue
    reponse = client_test.get(
        "/book/CompetitionInconnue/ClubTest",
        follow_redirects=True,
    )

    assert "Désolé, cette compétition n’a pas été trouvée." in reponse.get_data(
        as_text=True
    )

    # Reconnexion après le message d'erreur
    client_test.post(
        "/showSummary",
        data={"email": "club@test.com"},
    )

    # Accès à la compétition
    reponse = client_test.get("/book/CompetitionTest/ClubTest")

    assert "Places available: 25" in reponse.get_data(as_text=True)

    # Réservation de trois places
    reponse = client_test.post(
        "/purchasePlaces",
        data={
            "club": "ClubTest",
            "competition": "CompetitionTest",
            "places": "3",
        },
    )

    contenu_reponse = reponse.get_data(as_text=True)

    assert "Great-booking complete!" in contenu_reponse
    assert "Points available: 10" in contenu_reponse
    assert "Number of Places: 22" in contenu_reponse

    # Déconnexion
    reponse = client_test.get(
        "/logout",
        follow_redirects=True,
    )

    assert "Welcome to the GUDLFT Registration Portal!" in reponse.get_data(
        as_text=True
    )
