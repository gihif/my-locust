from locust import HttpLocust, TaskSet, task
from slumber import API 
import json, requests

nameInquiry = [{
                "score": 775,
                "userId": "600e74742a53bf9e0e58",
                "storeId": "test",
                "apiVersion": "1.0"
            }]
myheaders = {'Content-Type': 'application/json', 'Checksum': '8f9f393012097ef1e973d4ac89c84a269550732ddd6afe207e98b18b744f7059', 'Authorization': 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiI2MDBlNzQ3NDJhNTNiZjllMGU1OCIsInN0b3JlaWQiOiJ0ZXN0IiwiZXhwIjoxNjAxNTQxMDY5fQ.IP2p7peD_Y7j-YcRPXdf6uRx6Xw3ec7hDhoDAxbnIVM'}

class NameInquiries(TaskSet):
  @task(1)
  def send(self):
    response = self.client.post("/Game/Voucher", data=nameInquiry, headers=myheaders)

    print("Response status code:", response.status_code)
    print("Response content:", response.text)