#!/usr/bin/python3
from flask import Flask, request
app = Flask(__name__)
@app.route("/bobo") # le chemin pour acceder via nag url 
def main():
    q=3
    d=6
    j=q+d
    return (" le resultat est  {}".format(j)) # appel une fconction via le navig
if __name__ == "__main__":
    app.run(host='192.168.56.10', port=5000 , debug=True)   