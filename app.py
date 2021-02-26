import os
from flask import Flask
from flask import request
from flask import jsonify
from persongenerator import main  # this import is not working, why?

webapp = Flask(__name__)


@webapp.route('/', methods=['GET', 'POST'])
def listener():
    if request.method == 'GET':
        state_find = request.args.get("state")
        num_addr = request.args.get("nums")
        if not state_find or not num_addr:
            return "Error: Missing one or both required inputs"
        return_csv = 0
        adds_generated = main(state_find, num_addr, return_csv)
        return jsonify(adds_generated)
    if request.method == 'POST':
        state_find = request.args.get("state")
        num_addr = request.args.get("nums")
        if not state_find or not num_addr:
            return "Error: Missing one or both required inputs"
        return_csv = 0
        adds_generated = main(state_find, num_addr, return_csv)
        return jsonify(adds_generated)


if __name__ == '__main__':
    webapp.run()
