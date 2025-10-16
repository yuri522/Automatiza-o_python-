import tkinter as tk             # Importa tkinter para interface gráfica
from tkinter import Spinbox       # Importa Spinbox para seleção de números
import requests                   # Importa requests para fazer requisições HTTP
import threading                  # Importa threading para rodar funções em paralelo
from reportlab.lib.pagesizes import letter  # Importa tamanho de página para PDF
from reportlab.pdfgen import canvas         # Importa canvas para criar PDF

# Função principal que inicia o teste
def iniciar():
    url = entry_url.get()           # Pega o texto digitado no campo de URL
    qtd = int(spin_qtd.get())      # Pega a quantidade de requisições do Spinbox

    # Função que fará as requisições e gerará o PDF
    def testar():
        log_requisicoes = []        # Lista para guardar o status de cada requisição
        for i in range(1, qtd + 1): # Loop pelas requisições
            resposta = requests.get(url)                 # Faz requisição GET
            log_requisicoes.append(f"{i}: Status {resposta.status_code}") # Guarda resultado

        # Cria o PDF
        relatorio_pdf = canvas.Canvas("resultado_teste_estresse.pdf", pagesize=letter)
        relatorio_pdf.setFont("Helvetica", 12)                       # Define a fonte
        relatorio_pdf.drawString(50, 750, f"Teste de Estresse - URL: {url}")  # Título
        relatorio_pdf.drawString(50, 730, f"Total de Requisições: {qtd}")     # Quantidade

        posicao_y = 710                # Posição vertical inicial para escrever os logs
        for linha_log in log_requisicoes:   # Loop para escrever cada requisição no PDF
            relatorio_pdf.drawString(50, posicao_y, linha_log)      # Escreve linha
            posicao_y -= 15                                         # Move para próxima linha
            if posicao_y < 50:                                      # Se chegar no fim da página
                relatorio_pdf.showPage()                             # Cria nova página
                posicao_y = 750                                      # Reseta posição vertical

        relatorio_pdf.save()           # Salva o PDF
        print("PDF gerado: resultado_teste_estresse.pdf")  # Mensagem no console

    # Roda a função testar em uma thread separada (não trava a interface)
    threading.Thread(target=testar).start()

# --- Interface gráfica ---
root = tk.Tk()                     # Cria janela principal
root.title("Teste de Estresse")    # Título da janela
root.geometry("300x150")           # Tamanho da janela

tk.Label(root, text="Digite a URL:").pack()   # Label do campo URL
entry_url = tk.Entry(root)                     # Campo para digitar URL
entry_url.pack()                               # Adiciona à janela

tk.Label(root, text="Número de requisições:").pack()  # Label do Spinbox
spin_qtd = Spinbox(root, from_=1, to=1000)            # Spinbox para quantidade
spin_qtd.pack()                                       # Adiciona à janela
spin_qtd.delete(0, "end")                             # Limpa valor padrão
spin_qtd.insert(0, "10")                              # Coloca valor inicial 10

tk.Button(root, text="Enviar", command=iniciar).pack()  # Botão para iniciar teste

root.mainloop()    # Mantém a janela aberta
