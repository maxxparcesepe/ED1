// 1. Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// 2. Middleware
app.use(bodyParser.json());

// 3. In-memory "database" (or later switch to real DB)
let users = [];

// 4. Signup route
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
    res.status(201).send('User registered successfully.');
});

// 5. Login route
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    const user = users.find(u => u.username === username && u.password === password);
    if (!user) {
        return res.status(401).send('Invalid username or password.');
    }

    res.status(200).send('Login successful.');
});

// 6. Logout route (only makes sense if using sessions or tokens, simple version here)
app.post('/logout', (req, res) => {
    // In real app, you would clear the user's session or token.
    res.status(200).send('Logout successful.');
});

// 7. Start server
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
