import server


def test_refus_places_insuffisantes():
    # Vérification places dispos
    resultat = server.verifier_places_disponibles(4, 5)

    assert resultat is False
