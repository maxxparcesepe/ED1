// 1. Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// 2. Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files like HTML, CSS, JS
app.use(express.static('public'));

// 3. In-memory "database" (or later switch to real DB)
let users = [];

// Serve the login page at the root URL
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});


const path = require('path');

// ... inside your /signup route:
app.get('/signup', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'signup.html'));
});

  
// Signup route
app.post('/signup', (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.status(400).send('Username and password are required.');
    }

    const existingUser = users.find(u => u.username === username);
    if (existingUser) {
        return res.status(409).send('User already exists.');
    }

    users.push({ username, password });

    // Redirect to dashboard after successful signup
    res.redirect('/dashboard');
});


// 5. Login route
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    const user = users.find(u => u.username === username && u.password === password);
    if (!user) {
        return res.status(401).send('Invalid username or password.');
    }

    // If login is successful, redirect to dashboard
    res.redirect('/dashboard');
});


// 6. Logout route
app.post('/logout', (req, res) => {
    res.status(200).send('Logout successful.');
});

// Dashboard route - serve a simple dashboard page
app.get('/dashboard', (req, res) => {
    res.sendFile(__dirname + '/public/dashboard.html');
});

// 7. Start server
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});



