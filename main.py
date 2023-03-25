from flask import Flask, request, render_template

import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return render_template('index.html')

@app.route("/converter", methods=['POST'])
def converter():
    error = None
    if request.method == 'POST':
        if valida_valor_numerico(request.form['valor']):
            taxa_de_conversao = consultar_api((
                request.form['moeda_base'], request.form['moeda_target']
            ))
            valor_a_ser_convertido = float(request.form['valor'])
            valor_convertido = converter(valor_a_ser_convertido, taxa_de_conversao)
            return render_template('index.html', valor_convertido=valor_convertido)
        else:
            error = 'Valor deve ser um número'
    return render_template('index.html', error=error)

def valida_valor_numerico(valor):
    try:
        float(valor)
        return True
    except:
        return False
    
def consultar_api(moedas):
    data = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moedas[0]}-{moedas[1]}')
    data = data.json()
    return float(data[f'{moedas[0]}{moedas[1]}']['bid'])

def converter(valor_a_ser_convertido, taxa_de_conversao):
    return valor_a_ser_convertido * taxa_de_conversao

if __name__ == '__main__':
    app.run(debug=True, port=5000)