from flask import Flask,render_template,request
from flasgger import Swagger
import pickle
import sklearn
import numpy as np
import pandas as pd
pkl_import=open('cars.pkl','rb')
classifier=pickle.load(pkl_import)
app=Flask(__name__,template_folder="templates")
Swagger(app)
@app.route('/')
def base_route():
    return render_template("home.html")
@app.route("/hello/",methods=["GET"])

def hello():  
    """Lets Create some Swagger App
    -------
    parameters: 
    -   name: mpg
        in: query
        type: number
        required: true
    -   name: weight
        in: query
        type: number
        required: true
    -   name: cylinders
        in: query
        type: number
        required: true
    responses:
     200 :
        description : the result is

    """
    mpg = request.args.get("mpg")
    weight = request.args.get("weight")
    cylinders = request.args.get("cylinders")

    prediction = classifier.predict(np.array([[mpg,cylinders,weight]]))
    return str(prediction)
import os
#def hello(number):
 #   if number >= 10: return f"hello {number}",200
  #  if number < 10: return f"hello {number}",200
if __name__ == "__main__":
    #if os.environ('ENVIRONMENT')== "production":
        app.run()
#host='0.0.0.0', debug=True, port=80
