from flask import Flask, Response, render_template_string
import cv2
import numpy as np

app = Flask(__name__)

def detect_fire_smoke(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_fire = np.array([0, 50, 50])
    upper_fire = np.array([35, 255, 255])
    mask_fire = cv2.inRange(hsv, lower_fire, upper_fire)
    
    lower_smoke = np.array([0, 0, 100])
    upper_smoke = np.array([180, 50, 220])
    mask_smoke = cv2.inRange(hsv, lower_smoke, upper_smoke)
    
    mask = cv2.bitwise_or(mask_fire, mask_smoke)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    score = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 800:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            score = max(score, min(area/8000, 1.0))
    
    if score > 0.45:
        status = "HIGH RISK - FIRE/SMOKE"
        color = (0, 0, 255)
    elif score > 0.2:
        status = "MEDIUM RISK - Possible Smoke"
        color = (0, 165, 255)
    else:
        status = "NORMAL"
        color = (0, 255, 0)
    
    cv2.putText(frame, status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, color, 3)
    cv2.putText(frame, f"Confidence: {int(score*100)}%", (30, 90), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.85, color, 2)
    
    return frame

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        processed_frame = detect_fire_smoke(frame)
        ret, buffer = cv2.imencode(".jpg", processed_frame)
        frame_bytes = buffer.tobytes()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DisasterShield - Live Monitoring</title>
        <style>
            body { font-family: Arial; background: #0a2540; color: white; text-align: center; }
            h1 { color: #00ffcc; }
            .container { max-width: 1000px; margin: 20px auto; }
            img { border: 4px solid #00ffcc; border-radius: 10px; }
        </style>
    </head>
    <body>
        <h1>DisasterShield - SCAI 2026</h1>
        <h2>Real-time Multi-Hazard Detection System</h2>
        <div class="container">
            <img src="/video_feed" width="900">
        </div>
        <p><strong>Press Ctrl+C in terminal to stop server</strong></p>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    print("DisasterShield Dashboard Started!")
    print("Open Browser -> http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
