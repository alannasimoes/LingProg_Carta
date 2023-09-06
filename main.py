from flask import Flask, render_template, redirect, request
import funcionalidades
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("principal.html")

@app.route("/login/", methods = ['POST', 'GET'])
def login():

    if request.method == 'POST':
        login_input = request.form.get("nome")
        senha_input = request.form.get("senha")
        
        arq = open('login.txt', 'r')
        login = arq.readline()[7:-1]
        senha = arq.readline()[7:-1]
        arq.close()
        
        if login_input == login and senha_input == senha:
          return render_template('carta.html')
        else:
          return f'<h1>Usuário ou senha incorretos</h1>'

@app.route("/carta/", methods=['POST', 'GET'])
def carta():
  if request.method == "POST":
        opcao = request.form["botao"]
        if opcao == "Gerar Carta":
          data = request.form.get("data")
          destinatario = request.form.get("destinatario")
          mensagem = request.form.get("mensagem")
          remetente = request.form.get("remetente")
          carta_formatada = data + '\n' + destinatario + '\n' + mensagem + '\n' + remetente
          nome_arq = funcionalidades.salvar_txt(data, destinatario, remetente, carta_formatada)
          funcionalidades.salvar_pdf(nome_arq)
          return render_template("principal.html")
        else: 
          return render_template("principal.html")

if __name__ == '__main__':
  app.run(debug=True)