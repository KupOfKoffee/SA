from flask import Flask, request

app = Flask(__name__)

@app.route('/get_own_ip', methods=['GET'])
def get_own_ip():
    ip = request.remote_addr
    return f"My IP address is: {ip}"

if __name__ == '__main__':
    app.run(debug=True)
