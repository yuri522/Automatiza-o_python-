from locust import HttpUser, task, between
import random
import json

# CONFIGURAÇÃO BÁSICA
class UsuarioBase(HttpUser):
    # Marca a classe como abstrata para não ser instanciada diretamente
    abstract = True
    
    # Tempo de espera entre requisições (1-3 segundos)
    wait_time = between(1, 3)
    
    # URL base para os testes
    host = "http://localhost:8000" 

# TESTE DE CARGA
class UsuarioCarga(UsuarioBase):
    weight = 3 
    
    @task(3)
    def acessar_pagina_principal(self):
        self.client.get("/")
    
    @task(2)
    def buscar_dados_simples(self):
        self.client.get("/dados/busca?termo=teste")
    
    @task(1)
    def processar_requisicao_leve(self):
        dados = {"acao": "processar", "valor": 100}
        self.client.post("/processar", json=dados)

# TESTE DE ESTRESSE
class UsuarioEstresse(UsuarioBase):
    weight = 1
    
    @task(3)
    def processar_requisicao_complexa(self):
       # Operação mais pesada
        dados = {
            "acao": "processar_complexo",
            "valores": [random.randint(1, 1000) for _ in range(100)]
        }
        self.client.post("/processar/complexo", json=dados)
    
    @task(2)
    def buscar_dados_complexos(self):
         # Múltiplos parâmetros e Mais processamento
        self.client.get("/dados/busca/complexa?filtros=1,2,3,4,5")
    
    @task(1)
    def operacao_estressante(self):
        # Força o sistema com Processamento intensivo
        dados = {
            "acao": "estressar",
            "dados": [random.randint(1, 1000) for _ in range(500)]
        }
        self.client.post("/estressar", json=dados)

# TESTE DE VOLUME
class UsuarioVolume(UsuarioBase):
    weight = 1  
    
    @task(3)
    def enviar_grande_volume(self):
        # Muitos dados de uma vez
        dados = {
            "acao": "processar_volume",
            "dados": [random.randint(1, 1000) for _ in range(1000)]
        }
        self.client.post("/volume/enviar", json=dados)
    
    @task(2)
    def processar_lote_grande(self):
        # Simula processamento em lote com Operação em massa
        dados = {
            "acao": "processar_lote",
            "itens": [{"id": i, "valor": random.randint(1, 1000)} 
                     for i in range(100)]
        }
        self.client.post("/volume/lote", json=dados)
    
    @task(1)
    def operacao_volume_maximo(self):
        # Simula operação com volume máximo com Processamento massivo
        dados = {
            "acao": "volume_maximo",
            "dados": [random.randint(1, 1000) for _ in range(2000)]
        }
        self.client.post("/volume/maximo", json=dados)


# Uso:

# Execute o teste:

# locust -f teste_locust.py