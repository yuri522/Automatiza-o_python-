from flask import Flask, jsonify,request
import time
import random

app = Flask(__name__)

def simular_processamento():
    time.sleep(0.1)

@app.route('/')
def pagina_principal():
    simular_processamento()
    return jsonify({"Mensagem": "Pagina inicial"})

@app.route('/dados/busca')
def buscar_dados():
    simular_processamento()
    return jsonify({"resultado": {"item1" , "item2" , "item3" }})

@app.route('/dados/buscar/complexa')
def buscar_dados_complexo():
    simular_processamento()
    return jsonify ({"resultado": [{id: i, "valor": random.randint (1, 1000)} for i in range(5) ]})
                                                                                          

 
if __name__ == '__name__':
    app.run(port=8000)


