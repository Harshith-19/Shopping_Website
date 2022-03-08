import pickle
import json
from flask import Flask, render_template, request, jsonify   

@app.route("/history")
def history():
    c=0
    d=0
    for i in P:
        c+=i
    return render_template("history.html",c=c,P=P,d=d)
    
if __name__=="__main__":
    app.run()
