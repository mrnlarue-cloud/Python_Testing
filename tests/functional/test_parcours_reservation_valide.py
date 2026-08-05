# Permet à Python de piloter un véritable navigateur
from selenium import webdriver


def test_parcours_reservation_valide():
    navigateur = webdriver.Chrome()

    try:
        # Ouvre la page
        navigateur.get("http://127.0.0.1:5000")

        # vérification du chargement de la page d'accueil
        assert "GUDLFT Registration" in navigateur.title

    finally:
        # Fermeture automatique du navigateur
        navigateur.quit()
