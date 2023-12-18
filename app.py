from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/",  methods=['GET'])
def get_data():
    data = {"Data" : "Trash"}
    return jsonify(data)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
