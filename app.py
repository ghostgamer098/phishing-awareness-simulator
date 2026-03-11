from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def capture():
    email = request.form['email']

    with open("clicks.txt", "a") as f:
        f.write(email + "\n")

    return render_template("awareness.html")

if __name__ == "__main__":
    app.run(debug=True)