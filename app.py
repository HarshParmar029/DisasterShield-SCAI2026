from flask import Flask, Response, render_template_string
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="models/fire_smoke_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

IMG_SIZE = (160, 160)

def predict_frame(frame):
    img = cv2.resize(frame, IMG_SIZE)
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    interpreter.set_tensor(input_details[0]["index"], img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]["index"])
    prob = float(output[0][0])
    return prob

def annotate_frame(frame):
    prob = predict_frame(frame)

    # class_indices was {"fire_images": 0, "non_fire_images": 1}
    # sigmoid output close to 0 -> fire, close to 1 -> non-fire
    fire_confidence = 1.0 - prob

    if fire_confidence > 0.7:
        status = "HIGH RISK - FIRE DETECTED"
        color = (0, 0, 255)
    elif fire_confidence > 0.4:
        status = "MEDIUM RISK - Possible Fire"
        color = (0, 165, 255)
    else:
        status = "NORMAL"
        color = (0, 255, 0)

    cv2.putText(frame, status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 3)
    cv2.putText(frame, f"Confidence: {int(fire_confidence*100)}%", (30, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.85, color, 2)
    return frame

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        processed_frame = annotate_frame(frame)
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
        <h2>AI-Powered Real-time Fire Detection (MobileNetV2)</h2>
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
    print("DisasterShield Dashboard Started (AI Model)!")
    print("Open Browser -> http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
