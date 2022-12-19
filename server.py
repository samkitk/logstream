import os
import threading
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inito-assignment'
socketio = SocketIO(app)

# Add a global variable to keep track of whether the background thread is running
background_thread_running = False

def background_thread():
    """
    Function that runs in the background and periodically checks the log file for new lines.
    """
    global background_thread_running
    # Initialize the position to the end of the file
    position = os.stat('logs.txt').st_size
    while True:
        # Open the log file in read mode
        with open('logs.txt', 'r') as f:
            # Seek to the last known position in the file
            f.seek(position)
            # Read the lines in the file
            lines = f.readlines()
            # Emit a new_line event for each line
            for line in lines:
                socketio.emit('new_line', line)
            # Update the position to the end of the file
            position = f.tell()
        # Sleep for 1 second before checking the file again
        time.sleep(1)
    # Set the global variable to False when the thread finishes
    background_thread_running = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def healthcheck():
    return 'pong'

@socketio.on('connect')
def on_connect():
    print("New Client Connected")
    global background_thread_running
    # Start the background thread if it is not already running
    if not background_thread_running:
        t = threading.Thread(target=background_thread)
        t.start()
        background_thread_running = True

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=5000,allow_unsafe_werkzeug=True)