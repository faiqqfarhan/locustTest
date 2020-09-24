from locust import HttpUser, between, task
import string
import random

PD_SERVER = 'https://pd-pr83.sms.dev.unifonic.com/'

SECRETKEY = 'Yh3YkJvQ1CdqzOqptOzYNr154tKXTMB2'
ID = '100161'

class APIUser(HttpUser):
    wait_time = between(0, 2)

#GetAccount
@task()
def getAccount(self):
    url = PD_SERVER + "/provisioning/GetAccount"

    data = {
        "SecretKey": SECRETKEY,
        "ID": ID
    }
    self.client.post(url, data=data)

#GetChargingAccount
@task()
def getChargingAccount(self):
    url = PD_SERVER + "/charging/GetAccount"

    data = {
        "SecretKey": SECRETKEY,
        "ID": ID
    }
    self.client.post(url, data=data)
    
    #pulling from github


#pushing from pycharm