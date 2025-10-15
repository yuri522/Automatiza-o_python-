from locust import HttpUser, task, between
import random
import time

class usuario_base(HttpUser):
    abstract = True
    
    wait_time = between(1,3)

    host = "http://localhost:8000"

class UsuarioCarga(usuario_base):
    weight = 1
    
    @task(3)
    def acessar_pagina_principal(self):
        self.client.get("/")

    @task(2)
    def acessar_pagina_principal(self):
        self.client.get("/dados/busca/complexa?filtros=1,2,3")