import random

class SensorSimulator:
    def __init__(self):
        self.temperature = 28.0
        self.humidity = 65.0
        self.soil_moisture = 45.0
        self.rain = 0.0
        self.smoke_level = 0.0

    def update_sensors(self, fire_detected=False):
        if fire_detected:
            self.temperature = min(65, self.temperature + random.uniform(8, 15))
            self.humidity = max(10, self.humidity - random.uniform(5, 12))
            self.smoke_level = min(100, self.smoke_level + random.uniform(15, 30))
        else:
            self.temperature = max(20, self.temperature - random.uniform(0.5, 2))
            self.humidity = min(90, self.humidity + random.uniform(0.5, 3))
            self.smoke_level = max(0, self.smoke_level - random.uniform(5, 15))

        self.rain = random.uniform(0, 30) if random.random() > 0.85 else 0
        self.soil_moisture = max(10, min(90, self.soil_moisture + (self.rain * 0.8) - random.uniform(0.5, 2)))

        return self.get_readings()

    def get_readings(self):
        return {
            "temperature": round(self.temperature, 1),
            "humidity": round(self.humidity, 1),
            "soil_moisture": round(self.soil_moisture, 1),
            "rain": round(self.rain, 1),
            "smoke_level": round(self.smoke_level, 1)
        }

def calculate_risk(fire_confidence: float, sensors: dict):
    risk_score = 0

    if fire_confidence > 0.4 or sensors["smoke_level"] > 40:
        risk_score += 50
    if sensors["temperature"] > 45:
        risk_score += 30
    if sensors["rain"] > 15 and sensors["soil_moisture"] > 70:
        risk_score += 35
    if sensors["soil_moisture"] < 25 and sensors["temperature"] > 40:
        risk_score += 25

    final_risk = min(100, risk_score)

    if final_risk > 70:
        return "HIGH RISK", "Immediate Action Required", (0, 0, 255)
    elif final_risk > 40:
        return "MEDIUM RISK", "Monitor Closely", (0, 165, 255)
    else:
        return "LOW RISK", "Normal Conditions", (0, 255, 0)
