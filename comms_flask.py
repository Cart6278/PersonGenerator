import os
from flask import Flask
from flask import request
from flask import jsonify
from person-generator import main # this import is not working, why?

webapp = Flask(__name__)

@webapp.route('/get', methods=['GET'])
def listener():
    state_find = request.args.get("state")
    num_addr = request.args.get("nums")
    return_csv = 0
    if not state_find or not num_addr:
        return "Error: Missing one or both required inputs"

    adds_generated = main(state_find, num_addr, return_csv)
    return jsonify(adds_generated)

@webapp.route('/')
def index():
    return "This is the index"

if __name__ == '__main__':
    webapp.run(port=6001)