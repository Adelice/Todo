from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Todo

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todo_list = []
    for todo in todos:
        todo_list.append({
            'id': todo.id,
            'title':todo.title,
            'completed': todo.completed
        })
    return jsonify({'todos': todo_list})

if __name__ == '__main__':
    app.run(debug=True)
