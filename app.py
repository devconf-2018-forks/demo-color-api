#/usr/bin/python
from flask import Flask, jsonify, render_template
import os
import requests

app = Flask(__name__)

@app.route('/api/v1/colors')
def colors():
    backend_uri = "http://%s:8080" % os.environ["BACKEND_URI"]
    host = os.environ["HOSTNAME"]
    resp = requests.get("%s/api/v1/color" % backend_uri)
    data = resp.json()

    color = "#000000"
    if host.find("red") > -1:
      color = "#FF0000"
    elif host.find("blue") > -1:
      color = "#0000FF"
    elif host.find("green") > -1:
      color = "#00FF00"
    result = { "hostname": host, "color": color, "backend": data }
    print(result)
    return jsonify(result)

@app.route('/')
def index():
  return render_template("index.html", title="Hello World!")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)