#!flask/bin/python
from flask import Flask, jsonify, request, send_from_directory, render_template, redirect, url_for
import sys
import swarmCaller
import time
import json
	
app = Flask(__name__, static_folder='static')

@app.route('/api/v1/benchop', methods=['GET'])
def benchop():
	result = swarmCaller.benchop()
	return 'HTTP status 200 (OK) Please wait while the data is processed \n The data can be found by sending a GET request to /api/v1/result in about 5 minutes'

@app.route('/', methods=['GET'])
def sayHi():
	htmlstr = "<!DOCTYPE html> \n \
		<html> \n \
		<head> \n \
		<title>BENCHOP</title> \n \
		</head> \n \
		<body> \n \
		<h1>BENCHOP API</h1> \n \
		<p>Welcome to the BENCHOP API</p> \n \
		</body> \n \
		</html>"
	return htmlstr

@app.route('/api/v1/benchop', methods=['POST'])
def benchop_post():
	problems = request.form['problem'].split()
	methods = request.form['method'].split()
	result = swarmCaller.benchop(problems, methods)
	return 'HTTP OK 200 Please wait while the data is processed \n The data can be found by sending a GET request to /api/v1/result in about 5 minutes'

@app.route('/api/v1/result', methods=['GET'])
def result_get():
	result = swarmCaller.getResult()
	return result
	
@app.route('/api/v1/result', methods=['PUT'])
def result_put():
	result = swarmCaller.putResult()
	return 0
	
@app.route('/api/v1/result', methods=['DELETE'])
def apiDeleteResult():
	result = swarmCaller.deleteResult()
	return 'HTTP status 200 (OK)'

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)