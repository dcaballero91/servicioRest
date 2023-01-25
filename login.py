"""
Ejemplo:
Url: http://localhost:5000/login
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
from flask import Blueprint, request, jsonify
login = Blueprint('login', __name__)
@login.route('/login', methods=['POST'])
def llamarServicioSet():
    global user,passw
    ##try:
    user =request.json['pepe']
    passw =request.json['passw']

    print("Username",user)
    print("Password",passw)

    #inicializarVariables(categoryId)