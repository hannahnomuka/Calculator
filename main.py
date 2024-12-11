from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route("/text", methods=["GET", "POST"])
def text_editor():
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

    return render_template("text.html", result=result)

@app.route("/")
def home():
    # Add your own profile details here
    profile = {
        "name": "Hannah",
        "bio": "Aspiring Developer passionate about coding and creating awesome projects.",
        "profile_pic": "images/IMG_0132.jpeg",
        "github": "https://github.com/hannahnomuka",
        "projects": [
            {"name": "Calculator", "link": "https://hannahnomuka.pythonanywhere.com/calculator"},
            {"name": "Project 2", "link": "https://yourprojectlink2.com"},
            {"name": "Project 3", "link": "https://yourprojectlink3.com"}
        ]
    }
    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)
