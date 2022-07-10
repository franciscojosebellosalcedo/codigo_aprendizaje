
from threading import local
from flask import Flask,request
from flask import url_for
from flask import render_template
from flask import MySQL

apk=Flask(__name__)
apk.config['MYSQL_HOST']='localhost'
apk.config["MYSQL_USER"]="root"
apk.config["MYSQL_PASSWORD"]="developer2021"
apk.config["MYSQL_DB"]="registro_de_personas"
conexionMysql=MySQL(apk)


@apk.route("/home")
def index():
    return "inicio"

@apk.route("/agregar", methods=["post"])
def agregarPersona():
    nombre=request.form["nombre"]
    apellidos=request.form["apellidos"]
    edad=request.form["edad"]
    print(nombre,apellidos,edad)
    return "recibido"

@apk.route("/editar")
def editar():
    return "editar"

@apk.route("/eliminar")
def eliminar():
    return "Eliminar"

apk.run(port=5000,debug=True)