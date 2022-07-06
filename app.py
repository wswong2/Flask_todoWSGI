from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# ===============================================
# This is using a WSGI server for production
# ===============================================

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

# https://www.youtube.com/watch?v=Z1RJmh_OqeA
# https://github.com/jakerieger/FlaskIntroduction

class Todo(db.Model):
 	id=db.Column(db.Integer, primary_key=True)
 	content = db.Column(db.String(200), nullable=False)
 	date_created = db.Column(db.DateTime, default=datetime.utcnow)

 	# Please also change index.html line to <td>{{ task.date_created.date() }}</td>

 	# to change to get date, hr: min
 	#=================================================================
 	# time = datetime.utcnow().strftime('%B %d %Y - %H:%M')
 	# date_created = db.Column(db.String(), default=datetime.utcnow().strftime('%B %d %Y - %H:%M'))

 	def __repr__(self):
 		return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])

def index():
		if request.method =='POST':
	 		task_content=request.form['content']
	 		new_task=Todo(content=task_content)

	 		try:
	 			db.session.add(new_task)
	 			db.session.commit()
	 			return redirect('/')
	 		except:
	 			return 'There was an error adding to db !!!'

		else:
			tasks =Todo.query.order_by(Todo.date_created).all()

			return render_template('index.html', tasks=tasks)
			#return 'Hello'

@app.route('/delete/<int:id>')
def delete(id):
	task_to_delete=Todo.query.get_or_404(id)
	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return 'There was an error deleting from db !!!'

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
	task=Todo.query.get_or_404(id)
	if request.method=='POST':
		task.content=request.form['content']

		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'There was problem updating db'
	else:
		return render_template('update.html', task=task)

	

# ===============================================
# This is using a WSGI server for production
# ===============================================
from waitress import serve
    
if __name__=="__main__":
	serve(app, host='0.0.0.0', port=5000)
		    

	# app.run('0.0.0.0') # Works Okay!!!
	


