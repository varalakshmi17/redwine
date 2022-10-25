from flask import Flask,render_template,url_for,request,redirect
import numpy as np
import pandas as pd
import joblib
import pickle

app = Flask(__name__)

model = joblib.load("wineregressor.pkl")

@app.route("/")
@app.route("/main")
def main():
      return render_template("main.html")

@app.route("/pridict",methods=["POST"])


def predict():
       int_features = [[features for features in request.form.values()]]
       c = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
       'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
       'pH', 'sulphates', 'quality']
       df = pd.DataFrame(int_features, columns = c)
       final = df
       result = model.predict(final)
       print("Alcohol percentage is: ",result)

       return render_template("main.html", prediction_text="Alcohol Precentage is :{}".format(result))

if __name__=="__main__":
      app.debug=True 
      app.run()