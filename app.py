from flask import Flask, Response, render_template_string
import cv2
import numpy as np
import tensorflow as tf
from sensor_sim.fusion import SensorSimulator, calculate_risk

app = Flask(__name__)
sensor_sim = SensorSimulator()

interpreter = tf.lite.Interpreter(model_path="models/fire_smoke_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

IMG_SIZE = (160, 160)

def predict_fire(frame):
    img = cv2.resize(frame, IMG_SIZE).astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    interpreter.set_tensor(input_details[0]["index"], img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]["index"])
    prob = float(output[0][0])
    fire_confidence = 1.0 - prob  # 0=fire, 1=non_fire in class_indices
    return fire_confidence

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break

        fire_confidence = predict_fire(frame)
        sensors = sensor_sim.update_sensors(fire_confidence > 0.75)
        risk_level, message, color = calculate_risk(fire_confidence, sensors)

        cv2.putText(frame, risk_level, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, color, 3)
        cv2.putText(frame, f"Fire Conf: {int(fire_confidence*100)}%", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        cv2.putText(frame, f"Temp: {sensors['temperature']}C  Smoke: {sensors['smoke_level']}%", (30, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

        ret, buffer = cv2.imencode(".jpg", frame)
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")

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
        <h2>AI Model + Multi-Sensor Fusion Early Warning System</h2>
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
    print("DisasterShield Dashboard Started (AI + Sensor Fusion)!")
    print("Open Browser -> http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
