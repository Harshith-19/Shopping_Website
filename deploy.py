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
    
<<<<<<< HEAD
=======

@app.route("/policy")
def policy():
    return render_template("policy.html")
  
@app.route("/contact")
def contact():
    return render_template("contact.html")

>>>>>>> 76deb00 (New feature Integration)
if __name__=="__main__":
    app.run()
