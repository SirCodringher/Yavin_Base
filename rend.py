from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('glowna.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        message = request.form['text']
        print(message, flush=True)
        return render_template('submit.html')
    else:
        print('well', flush=True)
        return render_template('submit.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Logowanie poprawne!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Już zalogowany!")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
        # return f"<h1>{user}</h1>"
    else:
        flash("Nie jesteś zalogowany!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Wylogowanie poprawne, {user}!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
