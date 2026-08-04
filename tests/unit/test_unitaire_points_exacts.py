import server


def test_acceptation_points_exacts():
    # Vérifie que le nombre de points exact est accepté
    resultat = server.verifier_points_suffisants(5, 5)

    assert resultat is True
