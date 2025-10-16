from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

# Simula um pequeno delay para processamento
def simular_processamento():
    time.sleep(0.1)  # 100ms de processamento

@app.route('/')
def pagina_principal():
    simular_processamento()
    return jsonify({"mensagem": "Página principal"})

@app.route('/dados/busca')
def buscar_dados():
    simular_processamento()
    return jsonify({"resultados": ["item1", "item2", "item3"]})

@app.route('/dados/busca/complexa')
def buscar_dados_complexos():
    simular_processamento()
    return jsonify({"resultados": [{"id": i, "valor": random.randint(1, 1000)} for i in range(5)]})

@app.route('/processar', methods=['POST'])
def processar():
    simular_processamento()
    return jsonify({"status": "processado", "dados": request.json})

@app.route('/processar/complexo', methods=['POST'])
def processar_complexo():
    simular_processamento()
    return jsonify({"status": "processado", "dados": request.json})

@app.route('/estressar', methods=['POST'])
def estressar():
    simular_processamento()
    return jsonify({"status": "estressado", "dados": request.json})

@app.route('/volume/enviar', methods=['POST'])
def volume_enviar():
    simular_processamento()
    return jsonify({"status": "enviado", "dados": request.json})

@app.route('/volume/lote', methods=['POST'])
def volume_lote():
    simular_processamento()
    return jsonify({"status": "processado", "dados": request.json})

@app.route('/volume/maximo', methods=['POST'])
def volume_maximo():
    simular_processamento()
    return jsonify({"status": "processado", "dados": request.json})

if __name__ == '__main__':
    app.run(port=8000) 