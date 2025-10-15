from flask import Flask, jsonify,request
import time
import random

app = Flask(__name__)

def simular_processamento():
    time.sleep(0.1)

@app.route('/')
def pagina_principal():
    simular_processamento()
    return jsonify({"Mensagem: Pagina inicial"})
