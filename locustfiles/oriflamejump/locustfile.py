import time
from locust import HttpUser, task, between
import json, requests

payload = [{
            "score": 775,
            "userId": "600e74742a53bf9e0e58",
            "storeId": "test",
            "apiVersion": "1.0"
        }]
headers = {
    'Checksum': '8f9f393012097ef1e973d4ac89c84a269550732ddd6afe207e98b18b744f7059',
    'Authorization': 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiI2MDBlNzQ3NDJhNTNiZjllMGU1OCIsInN0b3JlaWQiOiJ0ZXN0IiwiZXhwIjoxNjAxNTQxMDY5fQ.IP2p7peD_Y7j-YcRPXdf6uRx6Xw3ec7hDhoDAxbnIVM',
    'Content-Type': 'application/json'
}

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    @task
    def images_page(self):
        #self.client.get("/Health/Database")
        #self.client.get("/Game/ListFile")
        self.client.post("/Game/Voucher", data=payload, headers=headers, catch_response=True)