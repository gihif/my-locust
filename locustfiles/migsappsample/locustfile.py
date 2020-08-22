import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def images_page(self):
#        self.client.get("/images.json")
        self.client.get("/health")