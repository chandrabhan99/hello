from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_hello():
    print("Hello world")
    return {"Message":"Hello world.."}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)