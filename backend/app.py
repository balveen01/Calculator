from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Add function
@app.route('/add', methods=['POST']) 
def add():
    # Get the first and second number from the form data and convert them to integers
    first_num = int(request.form['first_num'])
    second_num = int(request.form['second_num'])

    # Return the result of the addition
    return jsonify({
        "code": 200,
        "result": first_num + second_num
    }), 200

# Subtract function
@app.route('/subtract', methods=['POST']) 
def subtract():
    # Get the first and second number from the form data and convert them to integers
    first_num = int(request.form['first_num'])
    second_num = int(request.form['second_num'])

    # Return the result of the subtraction
    return jsonify({
        "code": 200,
        "result": first_num - second_num
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)