# DisasterShield — SCAI 2026

**AI-Powered Multi-Hazard Early Warning System with Edge Intelligence & Sensor Fusion**

**SCAI 2026** | **Track 1: Smart Sensing & Intelligent Electronic Systems**
**IEEE Student Branch, SVNIT Surat**

---

## Problem Statement

Climate change is increasing the frequency of natural disasters — floods, wildfires, and droughts — across India, causing heavy loss of life, crops, and property. Existing early-warning systems are often expensive, centralized, and too slow to give localized, real-time alerts to the communities that need them most.

---

## Proposed Solution

DisasterShield is a low-cost, AI-based multi-hazard early warning system that combines:

- Real-time fire/smoke detection using a trained deep learning model
- Multi-sensor data fusion for temperature, smoke, rain, and soil moisture trends
- A live web dashboard for monitoring and instant risk-level alerts

---

## Tech Stack

- **Language:** Python 3.13
- **Computer Vision:** OpenCV
- **AI/ML:** MobileNetV2 (Transfer Learning) + TensorFlow/Keras, converted to TensorFlow Lite
- **Dashboard:** Flask with live MJPEG video streaming
- **Sensor Fusion:** Custom rule-based + confidence engine

---

## Dataset

- Fire Dataset (Kaggle) — 755 fire images + 244 non-fire images
- Images resized to 160x160 with augmentation (rotation, zoom, flip)

---

## Model & Results

- **Base Model:** MobileNetV2 (ImageNet pretrained)
- **Training Accuracy:** ~99%
- **Validation Accuracy:** 96.98% - 97.99%
- **Model Size:** ~9.2 MB (TensorFlow Lite format) — edge-ready for Raspberry Pi

### Training Curves
![Training Curves](training_curves.png)

### Confusion Matrix
![Confusion Matrix](confusion_matrix.png)

### Sample Predictions
![Sample Predictions](sample_predictions.png)

**Multi-Hazard Risk Engine** — Camera (AI Vision) + Simulated Sensors (Temperature, Humidity, Smoke, Rain, Soil Moisture) fused into a single risk level (Low / Medium / High).

---

## Current Status (as of July 2026)

- [x] Environment setup and GitHub repo
- [x] Live camera pipeline with OpenCV
- [x] MobileNetV2 model trained and converted to TFLite
- [x] Flask dashboard with live video and risk overlay
- [x] Sensor simulation and intelligent fusion logic
- [ ] Real hardware integration (Raspberry Pi) — next step

---

## Project Structure
---

## How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open your browser to `http://127.0.0.1:5000`

---

## Support Requested

- Guidance on improving model robustness with more diverse non-fire training data
- Suggestions for budget-friendly real sensors (Raspberry Pi compatible)
- Feedback on the risk-fusion logic for flood/drought scenarios

---

## Why This Matters

DisasterShield aligns with SCAI 2026's theme "Connected Intelligence" — combining smart sensing, trained AI, and sensor fusion to build a system with real, localized societal impact for disaster response in vulnerable communities.

---

**Solo Developer:** Harsh C. Parmar
**Submitted for:** SCAI 2026 — Project Challenge & Technical Showcase
**IEEE Student Branch, SVNIT Surat**

Made with care for innovation and community safety.

## Presentation

[View Full Presentation (PDF)](DisasterShield_SCAI2026_Harsh_Parmar.pdf)

