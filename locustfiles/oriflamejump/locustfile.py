import logging
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    @task
    def index_page(self):
        newHeaders = {'Checksum': 'c127fb23709dfd79227d5a92a230bea8f635f2ac05c07eb6e0d26ad90d3d3a0f', 'Authorization': 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiI2MDBlNzQ3NDJhNTNiZjllMGU1OCIsInN0b3JlaWQiOiJ0ZXN0IiwiZXhwIjoxNjAxNjk4NzIwfQ.Uf5yqnAGFZkh5MgDMONDQhGYyZnrLhG21LVaSDI2KDY', 'Content-Type': 'application/json'}
        mydata = {"score":775, "userId":"600e74742a53bf9e0e58", "storeId":"test", "apiVersion":"1.0"}
        
        response = self.client.post("/Game/Voucher", json = mydata, headers = newHeaders)
        if response.status_code == 400:
            logging.info("failed : " + str(response.status_code))
            logging.info(response.json())
        elif response.status_code == 500:
            logging.info("failed : internal server error" + str(response.status_code))