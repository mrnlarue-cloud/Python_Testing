import server


def test_deduction_places():
    # Vérif places restantes
    resultat = server.calculer_places_restantes(25, 3)

    assert resultat == 22
