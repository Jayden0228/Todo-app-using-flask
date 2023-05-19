import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'todo.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        title = request.form['title']
        desc = request.form['desc']
        todo= Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template("index.html", alltodo=alltodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo =  Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods=['GET','POST'])
def update(sno):
    if request.method=="POST":
        title = request.form['title']
        desc = request.form['desc']
        todo =  Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo =  Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo)


@app.route("/search", methods=['GET','POST'])
def search():
    if request.method=="POST":
        search = request.form['search']
        alltodotitle = Todo.query.filter(Todo.title.contains(search)).all()
        alltododesc = Todo.query.filter(Todo.desc.contains(search)).all()
        return render_template("index.html", alltodo=alltodotitle+alltododesc)

    else:
        return "search"


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)