
from flask_mysqldb import MySQL
from flask import Flask, flash, redirect, render_template, request, url_for

app=Flask(__name__)
app.secret_key='mysecretkey'

def mysql_conexion():
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='developer2021'
    app.config['MYSQL_DB']='registro_de_personas'
    con=MySQL(app)
    return con
    
conexion=mysql_conexion()

@app.route('/')
def principal():
    cur=conexion.connection.cursor()
    cur.execute('select * from registro')
    datos=cur.fetchall()
    print(datos)
    return render_template('index.html',data=datos)

@app.route('/agregar_persona',methods=['POST'])
def agregar_persona():
    if(request.method=='POST'):
        nombres=request.form['nombres']
        apellidos=request.form['apellidos']
        edad=int(request.form['edad'])
        if(edad>=18):
            print(nombres,apellidos,edad)
            cur=conexion.connection.cursor()
            cur.execute('insert into registro (nombres,apellidos,edad) values (%s,%s,%s)',(nombres,apellidos,edad))
            conexion.connection.commit()
            flash('Se agrego axitosamente..')
        else:
            flash('no se agrego la persona')
    return redirect(url_for("principal"))
        
@app.route('/recibir_dato/<id>')
def obtener_datos(id):
    array=[]
    cur=conexion.connection.cursor()
    cur.execute(f'select * from registro where id={id}')
    conexion.connection.commit()
    array=lista_datos=cur.fetchall()
    print(array)
    if(len(array)>0):
        return render_template('editar_persona.html',lista=array)
    else:
        flash('no se pudo obtener los datos de la persona')

@app.route('/editar_persona/<id>',methods=['POST'])
def editar_persona(id):
    if(request.method=='POST'):
        nombres=request.form['nombres']
        apellidos=request.form['apellidos']
        edad=request.form['edad']
        id=int(id)
        if(id>0):
            cur=conexion.connection.cursor()
            cur.execute('update registro set nombres=%s,apellidos=%s,edad=%s where id=%s',(nombres,apellidos,edad,id))  
            if(conexion.connection.commit()==True):
                flash('actualizado exitosamente..')
    return redirect(url_for('principal'))

@app.route('/eliminar_persona/<id>')
def eliminar_persona(id):
    cur=conexion.connection.cursor()
    cur.execute(f'delete from registro where id={id}')
    cur.connection.commit()
    return redirect(url_for("principal"))

def pagina_no_existete(error):
    return redirect(url_for("principal"))

if(__name__=="__main__"):
    app.register_error_handler(404,pagina_no_existete)
    app.run(debug=True,port=5000)