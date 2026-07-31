import server


def test_affichage_public_points(monkeypatch):
    # Faux club pour le test
    clubs_tests = [
        {
            "name": "Club X",
            "email": "clubX@test.com",
            "points": "37",
        },
        {
            "name": "Club Y",
            "email": "clubY@test.com",
            "points": "70",
        },
    ]

    monkeypatch.setattr(server, "clubs", clubs_tests)

    # Test Flask
    client_test = server.app.test_client()

    # Accès direct à la page sans besoin de connexion
    reponse = client_test.get("/points-clubs")

    # Lecture contenu
    contenu_reponse = reponse.get_data(as_text=True)

    # Vérifications status et informations
    assert reponse.status_code == 200
    assert "Club X" in contenu_reponse
    assert "37" in contenu_reponse
    assert "Club Y" in contenu_reponse
    assert "70" in contenu_reponse
