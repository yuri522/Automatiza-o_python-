from locust import HttpUser, task, between
import random
import time

class usuario_base(HttpUser):
    abstract = True
    
    wait_time = between(1,3)

    host = "http://localhost:8000"

    