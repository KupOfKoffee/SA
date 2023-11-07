from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/palindrome/<string:text>', methods=['GET'])
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    if text == text[::-1]:
        return jsonify({"result": True})
    else:
        return jsonify({"result": False})

if __name__ == '__main__':
    app.run(debug=True)
