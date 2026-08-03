import server


def test_refus_plus_de_douze_places():
    # Vérifie qu'une réservation de plus de 12 places est refusée
    resultat = server.verifier_limite_places(13)

    assert resultat is False
