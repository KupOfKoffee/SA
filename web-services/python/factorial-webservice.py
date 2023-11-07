from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/factorial/<int:num>', methods=['GET'])
def factorial(num):
    if num < 0:
        return jsonify({"error": "Factorial is not defined for negative numbers."})
    elif num == 0 or num == 1:
        return jsonify({"result": 1})
    else:
        result = 1
        for i in range(2, num+1):
            result *= i
        return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
