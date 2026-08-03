import server


def test_refus_points_insuffisants():
    # Vérification points suffisants
    resultat = server.verifier_points_suffisants(4, 5)

    assert resultat is False
