from flask import Flask, render_template, request
# importing csv module
import csv
import sqlite3
global msg
app = Flask(__name__)


@app.route("/")
def index():
    title = "Home - About Me"
    data = {
        'title': title
    }
    return render_template("index.html", data=data)


@app.route("/adding_project")
def adding_project():
    title = "Adding Project Info"
    data = {
        'title': title
    }
    return render_template("adding_project.html", data=data)


@app.route("/skills")
def skills():
    title = "My Skills"
    filename = "my_skills.csv"
    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    data = {"title": title}
    return render_template("skills.html", data=data, rows=rows)


@app.route("/projects")
def projects():
    title = "My Projects Page"
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from projects")

    rows = cur.fetchall()
    data = {"title": title}
    return render_template("projects.html", data=data, rows=rows)


@app.route("/add_project", methods=['POST'])
def add_project():
    title = "Adding Project Info"
    if request.method == 'POST':
        try:
            project_name = request.form['project_name']
            project_tools = request.form['project_tools']
            project_desc = request.form['project_desc']
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO projects(project_name, project_tools, project_desc)VALUES(?, ?, ?)",
                            (project_name, project_tools, project_desc))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            data = {"title": title}
            return render_template("add_project.html", data=data, msg=msg)
            con.close()


if __name__ == "__main__":
    app.run(debug=True)
