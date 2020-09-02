import logging
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    @task
    def index_page(self):
        newHeaders = {'Checksum': '8f9f393012097ef1e973d4ac89c84a269550732ddd6afe207e98b18b744f7059', 'Authorization': 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiI2MDBlNzQ3NDJhNTNiZjllMGU1OCIsInN0b3JlaWQiOiJ0ZXN0IiwiZXhwIjoxNjAxNTQxMDY5fQ.IP2p7peD_Y7j-YcRPXdf6uRx6Xw3ec7hDhoDAxbnIVM', 'Content-Type': 'application/json'}
        mydata = {"score": 775, "userId": "600e74742a53bf9e0e58", "storeId": "test", "apiVersion": "1.0"}
        
        response = self.client.post("/Game/Voucher", json = mydata, headers = newHeaders)
        if response.status_code == 400:
            logging.info("failed : " + str(response.status_code))
            logging.info(response.json())
        elif response.status_code == 500:
            logging.info("failed : internal server error" + str(response.status_code))