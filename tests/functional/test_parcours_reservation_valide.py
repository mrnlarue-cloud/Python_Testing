# Permet à Python de piloter un véritable navigateur
from selenium import webdriver

# Permet de choisir comment rechercher un élément HTML
from selenium.webdriver.common.by import By


def test_parcours_reservation_valide():
    # Ouvre un navigateur Chrome
    navigateur = webdriver.Chrome()

    # Attend jusqu'à 10 secondes si un élément met du temps à apparaître
    navigateur.implicitly_wait(10)

    try:
        # Ouvre la page d'accueil de l'application
        navigateur.get("http://127.0.0.1:5000")

        # Vérifie que la page d'accueil est chargée
        assert "GUDLFT Registration" in navigateur.title

        # Recherche le champ e-mail avec son nom HTML
        champ_email = navigateur.find_element(By.NAME, "email")

        # Remplit l'e-mail
        champ_email.send_keys("john@simplylift.co")

        # Recherche le bouton de connexion
        bouton_connexion = navigateur.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        bouton_connexion.click()

        # Récupère le texte visible de la nouvelle page
        contenu_page = navigateur.find_element(By.TAG_NAME, "body").text

        # Vérifie que la connexion a réussi
        assert "john@simplylift.co" in contenu_page
        assert "Points available: 13" in contenu_page

        # Recherche le lien de réservation avec son texte visible
        lien_reservation = navigateur.find_element(By.LINK_TEXT, "Book Places")
        lien_reservation.click()

        # Récupère le texte de la page de réservation
        contenu_page = navigateur.find_element(By.TAG_NAME, "body").text

        # Vérifie la page de réservation
        assert "Spring Festival" in contenu_page
        assert "Places available: 25" in contenu_page

    finally:
        # Ferme toujours le navigateur
        navigateur.quit()
