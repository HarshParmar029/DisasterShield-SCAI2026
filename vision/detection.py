import cv2
import numpy as np
import time

def detect_fire_smoke(frame):
    """Improved Fire & Smoke Detection"""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Fire detection (Red-Orange range)
    lower_fire1 = np.array([0, 50, 50])
    upper_fire1 = np.array([35, 255, 255])
    mask_fire1 = cv2.inRange(hsv, lower_fire1, upper_fire1)
    
    # Smoke detection (Gray-White range)
    lower_smoke = np.array([0, 0, 100])
    upper_smoke = np.array([180, 50, 220])
    mask_smoke = cv2.inRange(hsv, lower_smoke, upper_smoke)
    
    # Combine masks
    mask = cv2.bitwise_or(mask_fire1, mask_smoke)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detection_score = 0
    alert_text = "NORMAL"
    color = (0, 255, 0)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 800:   # Minimum area threshold
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            detection_score = max(detection_score, min(area/5000, 1.0))
    
    if detection_score > 0.4:
        alert_text = "🚨 FIRE/SMOKE DETECTED!"
        color = (0, 0, 255)
    elif detection_score > 0.15:
        alert_text = "⚠️  Possible Smoke"
        color = (0, 165, 255)
    
    # Draw on frame
    cv2.putText(frame, alert_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                1.1, color, 3)
    cv2.putText(frame, f"Confidence: {int(detection_score*100)}%", (30, 90), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    return frame, detection_score > 0.3

# ============== LIVE DEMO ==============
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    
    print("DisasterShield Vision System Started... Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        processed_frame, alert = detect_fire_smoke(frame)
        
        cv2.imshow("DisasterShield - Live Detection", processed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        time.sleep(0.03)  # Smooth fps
    
    cap.release()
    cv2.destroyAllWindows()