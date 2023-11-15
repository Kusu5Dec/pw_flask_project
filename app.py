from flask import Flask,render_template
import requests
app=Flask(__name__)
@app.route("/")
def first():
    response=requests.get("https://api.covidtracking.com/v1/us/daily.json")
    data=response.json()
    return render_template('d1.html',Data=data)


    