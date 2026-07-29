from server import app


def test_email_inconnu_message_erreur():
    """Vérifie qu'un e-mail inconnu ne fait pas planter l'application."""

    # Création d'un client permettant de simuler des requêtes Flask.
    client_test = app.test_client()

    # Simulation de l'envoi du formulaire avec une adresse inconnue.
    reponse = client_test.post(
        "/showSummary",
        data={"email": "inconnu@exemple.com"},
        follow_redirects=True,
    )

    # Conversion du contenu de la réponse en texte lisible.
    contenu_reponse = reponse.get_data(as_text=True)

    # Vérification du statut et du message affiché.
    assert reponse.status_code == 200
    assert "Désolé, cette adresse e-mail n’a pas été trouvée." in contenu_reponse
