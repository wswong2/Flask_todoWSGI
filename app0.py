from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def index():
	return "Hello world Flask 1 !!!"



if __name__=="__main__":
	app.run(debug=True)



