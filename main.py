import os 
import json 
import requests 
from flask import Flask,render_template,url_for,redirect,request,jsonify 

app = Flask(__name__)

@app.route("/")
def index():


    return render_template("index.html")
@app.route("/modal")
def index2():
      return render_template("index2.html")

@app.route("/modal2")
def index3():
      return render_template("index3.html")
@app.route("/modal3")
def index4():
      return render_template("index4.html")
@app.route("/modal4")
def index5():
      return render_template("index5.html")
@app.route("/modal5")
def index6():
      return render_template("index6.html")
@app.route("/modal6")
def index7():
      return render_template("index7.html")
@app.route("/modal7")
def index8():
      return render_template("index8.html")
@app.route("/multi_agent_task",methods=['POST','GET'])
def multi_agent_data():
        reqdat  =  request.get_json(force=True)
        email = reqdat.get('email')
        project_name = reqdat.get('project_name')
        reqmulti_agent = requests.get('http://192.168.50.247:5959/total_task_agent').json()
        return reqmulti_agent[email][project_name]
if __name__ == "__main__":

       app.run(debug=True,threaded=True,host="0.0.0.0",port=5764)
