from locust import HttpUser, constant, task


class UtilisateurGUDLFT(HttpUser):

    # Attend 60 secondes avant de pouvoir refaire une réservation
    wait_time = constant(60)

    @task
    def reserver_place(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "club": "Simply Lift",
                "competition": "Spring Festival",
                "places": "1",
            },
        )
