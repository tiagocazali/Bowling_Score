from flask import Flask, render_template, request

app = Flask(__name__)

historico = []

@app.route('/')
def index():
    pontuacao_total = sum(pontuacao for _, _, pontuacao in historico)
    return render_template('index.html', historico=historico, pontuacao_total=pontuacao_total)

@app.route('/registrar_pinos', methods=['POST'])
def registrar_pinos():
    pinos_derrubados = int(request.form['pinos_derrubados'])
    
    # Aqui você pode adicionar a lógica para registrar os pinos derrubados
    # e calcular a pontuação parcial

    pontuacao_parcial = 0  # Atualize com sua lógica de pontuação parcial
    rodada = len(historico) + 1  # Número da rodada atual

    historico.append((rodada, pinos_derrubados, pontuacao_parcial))

    return render_template('index.html', historico=historico, pontuacao_total=0)

if __name__ == '__main__':
    app.run(debug=True)

