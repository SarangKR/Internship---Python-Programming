from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Validate user logic here
    return f"Welcome, {username}!"

if __name__ == "__main__":
    app.run(debug=True)
