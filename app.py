from flask import Flask, jsonify, request
from markupsafe import escape


# variables globales



# instanciar una clase 
app = Flask(__name__)

# crear la primer ruta
# decorador,la app, y la ruta es la url donde dirijiremos
@app.route('/')
# esta funcion va a funcionar cuando el usuario escriba /
def index():
    return 'Index'

# probar sintaxis
@app.route('/ping')
def ping():
    return jsonify({
        "message": "pong"
    })

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id":id})

@app.route('/recurso',methods= ['GET'])
def get_recursos():
    return jsonify({"data":"lista de todos los items de este recurso"})

@app.route('/recurso', methods=['POST'])
def post_recurso():
    print(request.get_json())
    # guardamos en una variable body la forma de poder entrar al request
    body = request.get_json()
    name= body["name"]
    modelo= body["modelo"]
# insertar en la base de datos 
    return jsonify({"data":{
        "name": name,
        "modelo":modelo
    }})

# un GET de 'recurso' a traves de su id
@app.route('/recurso/<int:id>', methods=['GET'])
def get_recurso_by_id(id):
    # buscar en la base ded atos un recurso con ese id
    return jsonify({'recurso':{
        "name":"nombre correspondiente a ese id",
        "modelo": "modelo correspondiente a ese id"
    }})




# el archivo debe funcionar correctamente si se lanza como archivo principal
if __name__ == '__main__':
    # pruebas en modo desarrollo
    app.run(debug=True, port=5000)

