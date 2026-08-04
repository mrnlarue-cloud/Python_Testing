import server


def test_acceptation_places_exactes():
    # Vérif acceptation du nombre exact
    resultat = server.verifier_places_disponibles(5, 5)

    assert resultat is True
