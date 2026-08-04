import server


def test_deduction_points():
    # Vérif des points restants
    resultat = server.calculer_points_restants(13, 3)

    assert resultat == 10
