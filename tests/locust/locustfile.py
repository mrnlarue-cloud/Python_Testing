from locust import HttpUser, between, task


class UtilisateurGUDLFT(HttpUser):

    # Attend entre 0,1 et 0,3 seconde avant de recommencer la tâche
    wait_time = between(0.1, 0.3)

    @task
    def consulter_competitions(self):
        # Envoie l'e-mail du club pour afficher la liste des compétitions
        self.client.post(
            "/showSummary",
            data={"email": "john@simplylift.co"},
        )
