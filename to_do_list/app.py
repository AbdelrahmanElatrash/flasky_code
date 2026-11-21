from flask import Flask , render_template, request, redirect, url_for, jsonify,abort  # pip install flask "psycopg[binary]"
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pas@localhost:5432/todo"
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.title}>'





def insert_data():
    " this function will seed mock data only if table is empty"

    data = Todo.query.all()  # 
    if data :
        return "there is row data in table"
    else:
        task1 = Todo(title='Buy groceries', description='Milk, Eggs, Bread', completed=False)
        task2 = Todo(title='Clean the house', description='Vacuum and dust', completed=False)
        task3 = Todo(title='Finish project', description='Complete the Flask app', completed=True)

        db.session.add(task1)
        db.session.add(task2)
        db.session.add(task3)
        db.session.commit()
    return "mock data was added to table"

with app.app_context():
    try:
        db.create_all()
        insert_data()
    except Exception as e :
        print(e)

@app.route('/')
def index():
    
    tasks = Todo.query.all()
    return render_template('index.html', tasks =tasks)

@app.route('/create', methods=['POST'])
def add_task():
    # title = request.form.get('title')
    # description = request.form.get('description')
    
    error = False
    body = {}
    
    
    try:
        title = request.get_json()['title']
        description = request.get_json()['description']
        task = Todo(title=title, description=description)

        db.session.add(task)
        db.session.commit()

        body["tile"] = title
        body["description"] = description
    except :
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else :
        # return redirect(url_for('index'))  # for form data handler
        # change return to be json , import jisonify from flask
        return jsonify({
            'title': task.title,
            'description': task.description,
        })


if __name__ == ("__main__"):
    app.run(port=5000)