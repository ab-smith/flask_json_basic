from flask import Flask,jsonify
import json

app = Flask(__name__)

@app.route("/", methods=('GET',))
def hello():
    return "App is Up!"

@app.route("/seclabels/<trigram>", methods=('GET',))
def secLabel(trigram):
    ret = ""
    with open('data.json') as json_file:  
        data = json.load(json_file)
        key = format(trigram).upper()
        if key in data:
            ret=data[key]
        else:
            ret="Unknown Product or not labelized."
    return jsonify(ret)

if __name__ == "__main__":
    app.run(host='0.0.0.0')