import server


def test_refus_reservation_places_indisponibles(monkeypatch):
    # Faux club de test avec assez de points
    clubs_test = [
        {
            "name": "Club Test",
            "email": "test@club.com",
            "points": "20",
        }
    ]

    # Fausse compétition avec seulement quatre places disponibles
    competition_test = [
        {
            "name": "Competition Test",
            "date": "2026-07-30 09:00:00",
            "numberOfPlaces": "4",
        }
    ]

    # Données remplacées test
    monkeypatch.setattr(server, "clubs", clubs_test)
    monkeypatch.setattr(server, "competitions", competition_test)

    client_test = server.app.test_client()

    # Tentative de réservation de cinq places
    reponse = client_test.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Competition Test",
            "places": "5",
        },
    )

    contenu_reponse = reponse.get_data(as_text=True)

    # Vérification du refus
    assert reponse.status_code == 200
    assert clubs_test[0]["points"] == "20"
    assert competition_test[0]["numberOfPlaces"] == "4"
    assert "Il n’y a pas assez de places disponibles." in contenu_reponse
    assert "Points restants du club: 20" in contenu_reponse
    assert "Places restantes pour Competition Test: 4" in contenu_reponse
