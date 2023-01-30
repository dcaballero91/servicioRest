"""
Ejemplo:
Url: http://localhost:5000/login
cURL -X PUT -d '{"user": "derlis", "passw": "123"}' -H "Content-Type: application/json" http://localhost:5001/login
Datos de entrada:
    
{
	"user":"derlis",
	"passw":"123"

}
Salida:
{"ParmOut": {
   "categoria": "Null",
   "codRes": "ERROR",
   "menRes": "No existe"
}}


"""
from ast import Str
from flask import Blueprint, request, jsonify
login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarServicioSet():
    global user,password
    ##try:
    #pediremos como dato de entrada user - pas
    user=request.json['user']
    password =request.json['password']
    inicializarVariables(user,password)
    
     
    salida = {'codRes': codRes, 'menRes': menRes, 'usuario':user,'accion':accion}
    return jsonify(salida)

def inicializarVariables(user,password):
    global codRes, menRes,accion
    userLocal="dcaballero"
    passLocal="unida123"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    try:
        print("Verificar login")
        if(str(password)==str(passLocal) and str(user)==str(userLocal)):
            print("Usuario y contraseña OK")
            accion="Succes"
        else:
            print("Usuario o contraseña incorrecta")
            accion="Usuario o contraseña incorrecta"

    except Exception as e:
        print("ERROR",str(e))
        codRes='ERROR'
        menRes='Msg'+str(e)