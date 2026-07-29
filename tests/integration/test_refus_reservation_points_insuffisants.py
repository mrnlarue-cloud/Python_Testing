import server


def test_refus_reservation_si_points_insuffisants(monkeypatch):
    # Faux club avec moins de points que de places demandées
    clubs_tests = [
        {
            "name": "Club Test",
            "email": "test@club.com",
            "points": "4",
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

    # Remplacement temporaire des données
    monkeypatch.setattr(server, "clubs", clubs_tests)
    monkeypatch.setattr(server, "competitions", competitions_tests)

    # Création du client de test Flask
    client_test = server.app.test_client()

    # Tentative de réservation de cinq places avec seulement quatre points
    reponse = client_test.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Competition Test",
            "places": "5",
        },
    )

    # Lecture du contenu renvoyé
    contenu_reponse = reponse.get_data(as_text=True)

    # Vérification du refus de la réservation
    assert reponse.status_code == 200
    assert clubs_tests[0]["points"] == "4"
    assert competitions_tests[0]["numberOfPlaces"] == "25"
    assert "Vous n’avez pas assez de points." in contenu_reponse
