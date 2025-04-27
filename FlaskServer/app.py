from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Load users from file if exists
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    return []

# Save users to file
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

# In-memory users (loaded from file)
users = load_users()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        for user in users:
            if user['username'] == username:
                return "User already exists", 409
        
        # Add new user
        users.append({'username': username, 'password': password})
        save_users(users)  # Save users to file
        
        return redirect(url_for('dashboard'))
    
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    for user in users:
        if user['username'] == username and user['password'] == password:
            return redirect(url_for('dashboard'))
    
    return "Invalid username or password", 401

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

