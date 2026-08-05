# Permet à Python de piloter un véritable navigateur
from selenium import webdriver

# Permet de choisir comment rechercher un élément HTML
from selenium.webdriver.common.by import By


def test_parcours_deconnexion():
    # Ouvre un navigateur
    navigateur = webdriver.Chrome()

    # Attend jusqu'à 10 secondes si un élément met du temps à apparaître
    navigateur.implicitly_wait(10)

    try:
        # Ouvre la page d'accueil de l'application
        navigateur.get("http://127.0.0.1:5000")

        # Recherche le champ e-mail avec son nom HTML
        champ_email = navigateur.find_element(By.NAME, "email")

        # Remplit l'e-mail
        champ_email.send_keys("john@simplylift.co")

        # Recherche le bouton de connexion
        bouton_connexion = navigateur.find_element(By.TAG_NAME, "button")
        bouton_connexion.click()

        # Recherche le lien de déconnexion avec son texte visible
        lien_deconnexion = navigateur.find_element(By.LINK_TEXT, "Logout")
        lien_deconnexion.click()

        # Récupère le texte visible de la page
        contenu_page = navigateur.find_element(By.TAG_NAME, "body").text

        # Vérifie le retour à la page d'accueil
        assert "Welcome to the GUDLFT Registration Portal!" in contenu_page

    finally:
        # Ferme toujours le navigateur
        navigateur.quit()
