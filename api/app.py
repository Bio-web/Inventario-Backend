from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

### Existencias
@app.route("/existencias/<code>", methods=['GET'])
def get_existencia(code):
    '''
    Consulta una sola existencia del inventario
    '''
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        existencias = dbinv.existencias
        response = app.response_class(
            response=dumps(existencias.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/existencias", methods=['GET'])
def get_existencias():
    '''
    Consulta todas las existencias del inventario
    '''
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        existencias = dbinv.existencias
        response = app.response_class(
            response=dumps(existencias.find()),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/existencias", methods=['POST'])
def create_existencia():
    '''
    Inserta un arreglo de existencias en la base de datos
    '''
    data = request.get_json()
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        existencias = dbinv.existencias
        existencias.insert(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/existencias/<code>", methods=['PUT'])
def update_existencia(code):
    '''
    Actualiza la informacion de una sola existencia en el inventario
    '''
    data = request.get_json()
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        existencias = dbinv.existencias
        existencias.update(
            {'_id': ObjectId(code)},
            data
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/existencias/<code>", methods=['DELETE'])
def delete_existencia(code):
    '''
    Elimina una sola existencia en el inventario identificada por ID
    '''
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        existencias = dbinv.existencias
        existencias.delete_one({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

### Proveedores
@app.route("/existencias/<code>", methods=['GET'])
def get_proveedor():
    '''
    Consulta un solo proveedor por ID
    '''
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        proveedores = dbinv.proveedores
        proveedores = app.response_class(
            response=dumps(proveedores.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/proveedores", methods=['GET'])
def get_proveedores():
    '''
    Consulta todos los proveedores del inventario
    '''
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        proveedores = dbinv.proveedores
        response = app.response_class(
            response=dumps(proveedores.find()),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/proveedores", methods=['POST'])
def create_proveedores():
    '''
    Inserta un arreglo de proveedores en la base de datos
    '''
    data = request.get_json()
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        proveedores = dbinv.proveedores
        proveedores.insert(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/proveedores/<code>", methods=['PUT'])
def update_proveedor(code):
    '''
    Actualiza la informacion de un solo proveedor en el inventario
    '''
    data = request.get_json()
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        proveedores = dbinv.proveedores
        proveedores.update(
            {'_id': ObjectId(code)},
            data
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/proveedores/<code>", methods=['DELETE'])
def delete_proveedor(code):
    '''
    Elimina un solo proveedor en el inventario identificada por ID
    '''
    con = db.get_connection()
    dbinv = con.dbinventario
    try:
        proveedores = dbinv.proveedores
        proveedores.delete_one({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")
