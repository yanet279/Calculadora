from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        operacion = request.json.get('operacion')
        resultado = eval(operacion)
        
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'error': 'Error en la operación, por favor intenta de nuevo.'})

if __name__ == '__main__':
    app.run(debug=True)