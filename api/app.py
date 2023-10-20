
import pickle
import warnings
from flask import Flask, render_template, request, jsonify

warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/prever', methods=['POST'])
def prever():
    
    arq = open('data/modelo_preco_imovel.pkl','rb')
    modelo = pickle.load(arq)
    arq.close()
    
    data = request.get_json()

    # Processa os dados do formulário e faz previsões usando o modelo
    # Retorna as previsões como JSON
    resultado = modelo.predict([data])[0]
    
    if resultado < 0.0:
        resultado = 0.0
    
    return jsonify({'previsao': resultado})

if __name__ == '__main__':
    app.run(debug=True)
