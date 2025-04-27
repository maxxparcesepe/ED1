from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory "database"
users = []

# Home route (login page)
@app.route('/')
def home():
    return render_template('index.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists
        for user in users:
            if user['username'] == username:
                return "User already exists", 409

        # Add new user
        users.append({'username': username, 'password': password})
        return redirect(url_for('dashboard'))
    
    return render_template('signup.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    for user in users:
        if user['username'] == username and user['password'] == password:
            return redirect(url_for('dashboard'))
    
    return "Invalid username or password", 401

# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Logout route
@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
