import server


def test_acceptation_douze_places():
    # Vérifie que 12 places sont autorisées
    resultat = server.verifier_limite_places(12)

    assert resultat is True
