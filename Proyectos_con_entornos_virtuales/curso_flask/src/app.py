
from flask import Flask, redirect, render_template, url_for

app=Flask(__name__)
@app.route("/home/")
def principal():
    
    return render_template("index.html")

def pagina_no_existente(error):
    return redirect(url_for("principal"))

if(__name__=="__main__"):
    app.register_error_handler(404,pagina_no_existente)
    app.run(debug=True,port=80)