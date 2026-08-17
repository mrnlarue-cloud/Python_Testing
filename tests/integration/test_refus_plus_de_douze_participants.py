import server


def test_refus_plus_de_douze_participants(monkeypatch):
    # Faux club de test avec assez de points
    clubs_test = [
        {
            "name": "Club Test",
            "email": "test@club.com",
            "points": "20",
        }
    ]

    # Fausse compétition
    competition_test = [
        {
            "name": "Competition Test",
            "date": "2026-07-30 09:00:00",
            "numberOfPlaces": "25",
        }
    ]

    # Données remplacées test
    monkeypatch.setattr(server, "clubs", clubs_test)
    monkeypatch.setattr(server, "competitions", competition_test)

    client_test = server.app.test_client()

    # Tentative de réservation de 13 places
    reponse = client_test.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Competition Test",
            "places": "13",
        },
    )

    contenu_reponse = reponse.get_data(as_text=True)

    # Vérification du refus
    assert reponse.status_code == 200
    assert clubs_test[0]["points"] == "20"
    assert competition_test[0]["numberOfPlaces"] == "25"
    assert "Vous ne pouvez pas réserver plus de douze places" in contenu_reponse
    assert "Points restants du club: 20" in contenu_reponse
    assert "Places restantes pour Competition Test: 25" in contenu_reponse
