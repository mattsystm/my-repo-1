from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def head():
    first = "This is my first conditions experience"
    return render_template("index.html", message=first)


@app.route("/gurkan")
def header():
    numbers = range(1,11)
    names = ["Ahmet", "Mehmet", "Hasan", "Huseyin"]
    return render_template("body.html", object=numbers)

if __name__ == "__main__":
    app.run(debug=True)