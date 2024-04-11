from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Função para validar o reCAPTCHA
def validar_recaptcha(chave_secreta, resposta_recaptcha):
    url = "https://www.google.com/recaptcha/api/siteverify"
    payload = {
        "secret": chave_secreta,
        "response": resposta_recaptcha
    }
    response = requests.post(url, data=payload)
    data = response.json()
    return data["success"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        chave_secreta = "SUA_CHAVE_SECRETA_DO_RECAPTCHA"
        resposta_recaptcha = request.form.get("g-recaptcha-response")

        # Validação do reCAPTCHA
        if validar_recaptcha(chave_secreta, resposta_recaptcha):
            # Redirecionar para o site externo ou realizar a segunda etapa de verificação
            return render_template("sucesso.html")
        else:
            # Voltar para a primeira etapa de verificação
            return render_template("falha.html")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9222)