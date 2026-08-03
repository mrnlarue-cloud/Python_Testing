import server
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


def test_connexion_reussie(monkeypatch):
    # Faux club adresse connue
    clubs_tests = [
        {
            "name": "Club Test",
            "email": "test@club.com",
            "points": "13",
        }
    ]

    # Fausse compèt
    competitions_tests = [
        {
            "name": "Competition Test",
            "date": "2026-08-03 10:00:00",
            "numberOfPlaces": "25",
        }
    ]

    # Remplacement des données
    monkeypatch.setattr(server, "clubs", clubs_tests)
    monkeypatch.setattr(server, "competitions", competitions_tests)

    client_test = server.app.test_client()

    # Connexion avec une adresse e-mail connue
    reponse = client_test.post(
        "/showSummary",
        data={"email": "test@club.com"},
    )

    # Lecture du contenu
    contenu_reponse = reponse.get_data(as_text=True)

    # Vérification de la connexion

    assert reponse.status_code == 200
    assert "test@club.com" in contenu_reponse
    assert "Points available: 13" in contenu_reponse
