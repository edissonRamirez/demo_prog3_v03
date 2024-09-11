from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludar():
    respuesta = {
        "mensaje":"hola mundo"
    }
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)