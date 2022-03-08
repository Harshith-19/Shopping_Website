import pickle
import json
from flask import Flask, render_template, request, jsonify   


@app.route("/policy")
def policy():
    return render_template("policy.html")

if __name__=="__main__":
    app.run()
