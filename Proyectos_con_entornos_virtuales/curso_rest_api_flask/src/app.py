from flask import Flask
import os

app=Flask(__name__)



if(__name__=="__main__"):
    os.system("cls")
    app.run(debug=True,port=5000)