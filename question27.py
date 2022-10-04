from flask import Flask, jsonify, request

import json

app = Flask(__name__)

glucose = [
    {
        "glucose_id": "2",
        "date" : "December/25/2022",
        "glucose" : "100mg"
    }
]

@app.route('/glucose/<int:glucose_id>', methods=['GET'])
def get_glucose(glucose_id):
    id = [ glucose[glucose_id]]
    return jsonify({"glucose":id})

if __name__== '__main__':
    app.run()