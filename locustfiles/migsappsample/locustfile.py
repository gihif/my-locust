import logging
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def images_page(self):
        self.client.get("/images.json")

    @task
    def upload_page(self):
        payload = {"image[title]": "Api Upload", "image[user_id]": "2"}
        files = {"image[picture]": open("/mnt/locust/devops.png","rb")}
        
        response = self.client.post("/images.json", data = payload, files = files)
        if response.status_code == 400:
            logging.info("failed : " + str(response.status_code))
            logging.info(response.json())
        elif response.status_code == 500:
            logging.info("failed : internal server error" + str(response.status_code))