from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

tasks = []

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = "d08a9771ceb45a228e218dab149857bd"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


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

@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form.get("city")
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        print(data)  # Debugging: Print API response

        if response.status_code == 200:
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }
            return render_template("weather.html", weather=weather)
        else:
            return render_template("weather_form.html", error=data.get("message", "City not found!"))

    return render_template("weather_form.html")




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
            {"name": "Weather", "link": url_for("weather")}
        ]
    }
    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)
