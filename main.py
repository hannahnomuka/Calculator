from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            # Perform the calculation based on the operation
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Please enter valid numbers."

    return render_template("calculator.html", result=result)

@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("todo.html", tasks=tasks)

@app.route("/")
def home():
    # Add your own profile details here
    profile = {
        "name": "Hannah",
        "bio": '''Aspiring Developer passionate about coding and creating awesome projects to express their feelings, life, and sharing it to people.''',
        "profile_pic": "images/IMG_0132.jpeg",
        "github": "https://github.com/hannahnomuka",
        "projects": [
            {"name": "Calculator", "link": "https://hannahnomuka.pythonanywhere.com/calculator"},
            {"name": "To-Do List", "link": url_for("todo")},
            {"name": "Project 3", "link": "https://yourprojectlink3.com"}
        ]
    }
    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)
