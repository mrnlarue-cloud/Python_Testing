# =========================
# IMPORTS
# =========================

# Permet à Python de piloter un véritable navigateur
from selenium import webdriver

# Permet de choisir comment rechercher un élément HTML
from selenium.webdriver.common.by import By

# =========================
# TEST DU PARCOURS DE RÉSERVATION
# =========================


def test_parcours_reservation_valide():
    # =========================
    # OUVERTURE DU NAVIGATEUR
    # =========================

    # Ouvre un navigateur Chrome
    navigateur = webdriver.Chrome()

    # Attend jusqu'à 10 secondes si un élément met du temps à apparaître
    navigateur.implicitly_wait(10)

    try:
        # =========================
        # OUVERTURE DE L'APPLICATION
        # =========================

        # Ouvre la page d'accueil de l'application
        navigateur.get("http://127.0.0.1:5000")

        # Vérifie que la page d'accueil est chargée
        assert "GUDLFT Registration" in navigateur.title

        # =========================
        # CONNEXION DU CLUB
        # =========================

        # Recherche le champ e-mail avec son nom HTML
        champ_email = navigateur.find_element(By.NAME, "email")

        # Remplit l'e-mail
        champ_email.send_keys("john@simplylift.co")

        # Recherche le bouton de connexion
        bouton_connexion = navigateur.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )

        # Clique sur le bouton de connexion
        bouton_connexion.click()

        # Attend que le lien de réservation apparaisse
        lien_reservation = navigateur.find_element(By.LINK_TEXT, "Book Places")

        # Récupère le texte visible de la nouvelle page
        contenu_page = navigateur.find_element(By.TAG_NAME, "body").text

        # Vérifie que la connexion a réussi
        assert "john@simplylift.co" in contenu_page
        assert "Points available: 13" in contenu_page

        # =========================
        # ACCÈS À LA RÉSERVATION
        # =========================

        # Clique sur le lien de réservation
        lien_reservation.click()

        # Recherche le champ de réservation
        champ_places = navigateur.find_element(By.NAME, "places")

        # Récupère le texte de la page de réservation
        contenu_page = navigateur.find_element(By.TAG_NAME, "body").text

        # Vérifie la page de réservation
        assert "Spring Festival" in contenu_page
        assert "Places available: 25" in contenu_page

        # =========================
        # RÉSERVATION D'UNE PLACE
        # =========================

        # Demande une place
        champ_places.send_keys("1")

        # Recherche le bouton de réservation
        bouton_reservation = navigateur.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )

        # Clique sur le bouton de réservation
        bouton_reservation.click()

        # Attend le retour sur la page des compétitions
        navigateur.find_element(By.LINK_TEXT, "Logout")

        # =========================
        # VÉRIFICATION DU RÉSULTAT
        # =========================

        # Récupère le résultat de la réservation
        contenu_page = navigateur.find_element(By.TAG_NAME, "body").text

        # Vérifie que la réservation a réussi
        assert "Great-booking complete!" in contenu_page

        # Vérifie que le point utilisé a bien été retiré
        assert "Points available: 12" in contenu_page

    finally:
        # =========================
        # FERMETURE DU NAVIGATEUR
        # =========================

        # Ferme toujours le navigateur
        navigateur.quit()
