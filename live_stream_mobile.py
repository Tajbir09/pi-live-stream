import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Uncomment the following lines if the libraries are not already installed
#install('flask')
#install('opencv-python')






from flask import Flask, Response, render_template_string
import cv2
import threading
import socket

app = Flask(__name__)

# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 is the default camera

# Check if the camera opened successfully
if not camera.isOpened():
    raise IOError("Cannot open webcam")

def get_ip_address():
    """Function to get the Raspberry Pi's IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def generate_frames():
    """Generator function to capture and encode video frames."""
    while True:
        # Read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # Resize frame for better performance on mobile
            frame = cv2.resize(frame, (640, 480))
            
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame = buffer.tobytes()

            # Yield the output frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Home page route that displays the video stream."""
    ip_address = get_ip_address()
    port = 5000
    # Responsive HTML template for mobile devices
    return render_template_string('''
        <!DOCTYPE html>
        <html>
            <head>
                <title>Raspberry Pi Live Video Stream</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body { text-align: center; background-color: #f0f0f0; }
                    h1 { color: #333; }
                    img { max-width: 100%; height: auto; }
                    .info { margin-top: 20px; font-size: 1em; color: #555; }
                </style>
            </head>
            <body>
                <h1>Live Video Stream</h1>
                <img src="{{ url_for('video_feed') }}" alt="Live Stream">
                <div class="info">
                    <p>Access the stream from your mobile device:</p>
                    <p>http://{{ ip }}:{{ port }}/</p>
                </div>
            </body>
        </html>
    ''', ip=ip_address, port=port)

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def run_flask():
    """Function to run the Flask app."""
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)

if __name__ == '__main__':
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
