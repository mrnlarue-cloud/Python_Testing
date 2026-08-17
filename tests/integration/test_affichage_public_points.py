import server


def test_affichage_public_points(monkeypatch):
    # Faux clubs pour le test
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

    # Client de test Flask
    client_test = server.app.test_client()

    # Vérification du lien sur la page d'accueil
    reponse = client_test.get("/")
    contenu_reponse = reponse.get_data(as_text=True)

    assert "/points-clubs" in contenu_reponse

    # Accès à la page publique des points
    reponse = client_test.get("/points-clubs")
    contenu_reponse = reponse.get_data(as_text=True)

    # Vérification des points affichés
    assert reponse.status_code == 200
    assert "Club X" in contenu_reponse
    assert "37" in contenu_reponse
    assert "Club Y" in contenu_reponse
    assert "70" in contenu_reponse
