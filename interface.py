from flask import Flask,jsonify,request
from project_app.utils import Medical

app=Flask(__name__)

@app.route("/")
def home():
    return "wel_come"

@app.route("/charge")
def next():
    age=45
    sex="female"
    bmi=5.67
    children=2
    smoker="no"
    region="southeast"


    med=Medical(age,sex,bmi,children,smoker,region)
    result=med.predict_charge()

    return jsonify({"msg":f"your charges is {result}"})

if __name__ == "__main__":
    app.run()         