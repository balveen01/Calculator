from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['POST']) 
def add():
    first_num = int(request.form['first_num'])
    second_num = int(request.form['second_num'])

    return jsonify({
        "code": 200,
        "result": first_num + second_num
    }), 200


@app.route('/subtract', methods=['POST']) 
def subtract():
    first_num = int(request.form['first_num'])
    second_num = int(request.form['second_num'])

    return jsonify({
        "code": 200,
        "result": first_num - second_num
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)