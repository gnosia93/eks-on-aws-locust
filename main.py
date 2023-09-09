import json
from locust import HttpUser,  task , between

class sample(HttpUser):
	wait_time = between(1, 3)
	access_token = ""
	def on_start(self):		
		print("start test")		

	def on_stop(self):		
		print("end test")		

	@task
	def add(self):
		data = {	
		    	"password": "7771",
			"name": "111",
    			"phoneNumber": "9-111-11",
    			"emailAddress": "9999@example.com"
		}
		self.client.post("/member/add", json.dumps(data), headers={"Content-Type" : "application/json"})

	@task
	def get(self):
		self.client.get("/member/1", headers={"Content-Type" : "application/json"})