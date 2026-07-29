import server


def test_diminution_points_reservation(monkeypatch):
    # Faux club
    clubs_tests = [
        {
            "name": "Club Test",
            "email": "test@club.com",
            "points": "13",
        }
    ]

    # Fausse compétition
    competitions_tests = [
        {
            "name": "Competition Test",
            "date": "2026-07-29 14:00:00",
            "numberOfPlaces": "25",
        }
    ]

    # Remplacement temporaire des données réelles de l'application
    monkeypatch.setattr(server, "clubs", clubs_tests)
    monkeypatch.setattr(server, "competitions", competitions_tests)

    # Création du client de test Flask
    client_test = server.app.test_client()

    # Simulation d'une réservation de trois places
    reponse = client_test.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Competition Test",
            "places": "3",
        },
    )

    # Lecture du contenu renvoyé
    contenu_reponse = reponse.get_data(as_text=True)

    # Vérification de la réponse et du nouveau solde de points
    assert reponse.status_code == 200
    assert "Points available: 10" in contenu_reponse
