import json
from locust import HttpUser, task, between
from faker import Faker
import base64

class sample(HttpUser):
	wait_time = between(1, 3)
	access_token = ""
	
	def on_start(self):
		print("start test")
		self.faker = Faker('ko-KR')

	def on_stop(self):		
		print("end test")		

	@task
	def add(self):
		name = self.faker.name()
		data = {	
		    "password": base64.b64encode(name.encode('utf-8')).decode('utf-8'),
		    "name": name,
	 	    "phoneNumber": self.faker.phone_number(),
    	  	    "emailAddress": self.faker.email()
		}
		self.client.post("/member/add", json.dumps(data), headers={"Content-Type" : "application/json"})

	@task
	def get(self):
		self.client.get("/member/1", headers={"Content-Type" : "application/json"})


