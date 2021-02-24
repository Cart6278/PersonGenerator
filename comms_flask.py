import os
from flask import Flask
from flask import request
from person-generator import main

webapp = Flask(__name__)

@webapp.route('/', methods=['GET'])
def listener():
    state_find = request.args.get("state")
    num_addr = request.args.get("nums")
    return_csv = 0
    if not state_find or not num_addr:
        return "Error: Missing one or both required inputs"

    csv_generated = main(state_find, num_addr, return_csv)