#this is a comment

from flask import Flask, render_template, jsonify

app = Flask(__name__)

#Instructions 1 and 4
@app.route('/')
def index():
	#return "Hello World"
	return render_template('home.html')

#Instruction 2
@app.route('/birthday')
def birthday():
	return "August 13 1997"

#Instruction 3
@app.route('/greeting/<name>')
def greeting(name):
	return "Hello " + name

#Extra Credit 1
@app.route('/add/<integer1>/<integer2>')
def add(integer1, integer2):
	integer1 = int(integer1)
	integer2 = int(integer2)
	result = integer1 + integer2
	result = str(result)
	return result

#Extra Credit 2
@app.route('/multiply/<integer1>/<integer2>')
def multiply(integer1, integer2):
	integer1 = int(integer1)
	integer2 = int(integer2)
	result = integer1 * integer2
	result = str(result)
	return result	

@app.route('/substract/<integer1>/<integer2>')
def substract(integer1, integer2):
	integer1 = int(integer1)
	integer2 = int(integer2)
	result = integer1 - integer2
	result = str(result)
	return result	

#Extra Credit 3
@app.route('/favoritefoods')
def favoritefoods():
	myFavoriteFoods = ["Burguers", "PB and Jelly Sandwiches", "Oatmeal"]
	return jsonify(myFavoriteFoods)