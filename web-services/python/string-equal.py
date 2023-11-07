from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/string_equality/<string:str1>/<string:str2>', methods=['GET'])
def string_equality(str1, str2):
    if str1 == str2:
        return jsonify({"result": True})
    else:
        return jsonify({"result": False})

if __name__ == '__main__':
    app.run(debug=True)
