from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classificar_num', methods=['POST'])
def classificar_num():
    try:
        num = int(request.form['num'])
        if num > 0:
            analise1 = "Positivo"
        elif num < 0:
            analise1 = "Negativo"
        elif num == 0:
            analise1 = "Zero"

        if num % 2 == 0:
            analise2 = "Par"
        else:
            analise2 = "Ímpar"

        return render_template('index.html', analise1=analise1, analise2=analise2)
    except Exception as e:
        analise1 = f"Ocorreu um erro inesperado {e}"
        analise2 = f"Ocorreu um erro inesperado {e}"
        return render_template('index.html', analise1=analise1, analise2=analise2)

if __name__ == '__main__':
    app.run(debug=True)