from flask import Flask, render_template

app = Flask(__name__)
# creating an app instance

# use a decorator @ to define the route for our webpage
@app.route("/")
#setting up a default page
def index():
    return "Welcome to DevOps team"

@app.route("/welcome/")
def welcome():
    return f"Welcome on board"

@app.route("/home/")
def home():
    return render_template("index.html")

# create 2 more pages/routes and add the functionality for email and password
# implement OOP inheritance

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/profile/")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)
