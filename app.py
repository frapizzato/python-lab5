from flask import Flask, render_template, request, redirect, url_for
from db_interact import show_all, insert_task,delete_task

app = Flask(__name__)


@app.route('/')
def home_redirect():
    return redirect(url_for("home"))

@app.route('/home')
def home():
    tasks = show_all()
    return render_template('home.html',task_list=tasks)

@app.route('/delete_page/<id_task>')
def delete_page(id_task):
    delete_task(id_task)
    return redirect(url_for("home"))

@app.route('/addTask',methods=['POST'])
def addTask():
    description = request.form['description']
    urgency = request.form['urgency']
    insert_task(description,urgency)
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()
