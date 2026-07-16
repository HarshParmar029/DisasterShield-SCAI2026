# DisasterShield — SCAI 2026

**AI-Powered Multi-Hazard Early Warning System with Edge Intelligence & Remote Sensing**

**SCAI 2026** | **Track 1: Smart Sensing & Intelligent Electronic Systems**
**IEEE Student Branch, SVNIT Surat**

---

## 🧭 Problem Statement

Climate change is increasing the frequency of natural disasters — floods, wildfires, droughts — across India, causing heavy loss of life, crops, and property. Existing early-warning systems are often expensive, centralized, and too slow to give localized, real-time alerts to the communities that need them most.

## 💡 Proposed Solution

DisasterShield aims to be a **low-cost, edge-AI based multi-hazard detection system** that combines:
- Real-time computer vision (smoke/fire detection)
- Lightweight deep learning models deployable on edge hardware
- Multi-sensor data fusion for flood/drought risk
- Remote sensing (NDVI-style) analysis for wider-area context

The goal is a system that works **offline**, is **cheap to deploy**, and gives **localized alerts** faster than traditional infrastructure.

## 🛠 Planned Tech Stack

- **Language:** Python 3
- **Computer Vision:** OpenCV
- **AI/ML:** Lightweight CNN (MobileNet-based), converted to TensorFlow Lite for edge inference
- **Data Fusion:** Rule-based + ML hybrid logic for combining sensor + vision signals
- **Dashboard/Alerts:** Flask-based web dashboard
- **Datasets (identified):**
  - Kaggle Wildfire Dataset (smoke & fire images/video)
  - PlantVillage Dataset (for future crop-stress extension)
  - Synthetic sensor data (DHT22, soil moisture, rain, MQ-135) for flood/drought simulation

## 📊 Current Status (as of July 2026)

This project is in the **planning and design phase**. Problem scoping, track alignment, dataset identification, and system architecture are complete. Implementation is starting now, guided by the SCAI workshop series (Basic Electronics, Python + OpenCV, ML Frameworks, DL Architectures).

**Immediate next steps:**
- [ ] Set up repo structure and environment
- [ ] Build initial OpenCV pipeline for smoke/fire detection on sample data
- [ ] Train a first-pass lightweight CNN on the Kaggle Wildfire dataset
- [ ] Build sensor-data simulation module for flood/drought logic
- [ ] Basic Flask dashboard for visualizing detections/alerts

## 📁 Planned Project Structure

```
DisasterShield-SCAI2026/
├── vision/          # OpenCV detection scripts
├── models/          # TF Lite models
├── sensor_sim/      # Simulated sensor data & fusion logic
├── dashboard/       # Flask web interface
├── notebooks/       # Training/experiment notebooks
├── utils/           # Helper functions & alert logic
├── main.py
├── requirements.txt
└── README.md
```

## 🙋 Support Requested

- Guidance on optimized lightweight CNN architectures for edge deployment (Raspberry Pi 4/5 class hardware)
- Suggestions for better/alternative datasets beyond Kaggle Wildfire for robustness
- Best practices for sensor data simulation that realistically mimics field noise

## 🎯 Why This Matters

DisasterShield directly aligns with SCAI 2026's theme of **Connected Intelligence** — bringing together smart sensing, edge AI, and remote sensing to build systems with real, localized societal impact.

---
# DisasterShield — SCAI 2026

**AI-Powered Multi-Hazard Early Warning System with Edge Intelligence & Remote Sensing**

**SCAI 2026** | **Track 1: Smart Sensing & Intelligent Electronic Systems**
**IEEE Student Branch, SVNIT Surat**

---

## 🧭 Problem Statement

Climate change is increasing the frequency of natural disasters — floods, wildfires, droughts — across India, causing heavy loss of life, crops, and property. Existing early-warning systems are often expensive, centralized, and too slow to give localized, real-time alerts to the communities that need them most.

## 💡 Proposed Solution

DisasterShield aims to be a **low-cost, edge-AI based multi-hazard detection system** that combines:
- Real-time computer vision (smoke/fire detection)
- Lightweight deep learning models deployable on edge hardware
- Multi-sensor data fusion for flood/drought risk
- Remote sensing (NDVI-style) analysis for wider-area context

The goal is a system that works **offline**, is **cheap to deploy**, and gives **localized alerts** faster than traditional infrastructure.

## 🛠 Planned Tech Stack

- **Language:** Python 3
- **Computer Vision:** OpenCV
- **AI/ML:** Lightweight CNN (MobileNet-based), converted to TensorFlow Lite for edge inference
- **Data Fusion:** Rule-based + ML hybrid logic for combining sensor + vision signals
- **Dashboard/Alerts:** Flask-based web dashboard
- **Datasets (identified):**
  - Kaggle Wildfire Dataset (smoke & fire images/video)
  - PlantVillage Dataset (for future crop-stress extension)
  - Synthetic sensor data (DHT22, soil moisture, rain, MQ-135) for flood/drought simulation

## 📊 Current Status (as of July 2026)

This project is in the **planning and design phase**. Problem scoping, track alignment, dataset identification, and system architecture are complete. Implementation is starting now, guided by the SCAI workshop series (Basic Electronics, Python + OpenCV, ML Frameworks, DL Architectures).

**Immediate next steps:**
- [ ] Set up repo structure and environment
- [ ] Build initial OpenCV pipeline for smoke/fire detection on sample data
- [ ] Train a first-pass lightweight CNN on the Kaggle Wildfire dataset
- [ ] Build sensor-data simulation module for flood/drought logic
- [ ] Basic Flask dashboard for visualizing detections/alerts

## 📁 Planned Project Structure

```
DisasterShield-SCAI2026/
├── vision/          # OpenCV detection scripts
├── models/          # TF Lite models
├── sensor_sim/      # Simulated sensor data & fusion logic
├── dashboard/       # Flask web interface
├── notebooks/       # Training/experiment notebooks
├── utils/           # Helper functions & alert logic
├── main.py
├── requirements.txt
└── README.md
```

## 🙋 Support Requested

- Guidance on optimized lightweight CNN architectures for edge deployment (Raspberry Pi 4/5 class hardware)
- Suggestions for better/alternative datasets beyond Kaggle Wildfire for robustness
- Best practices for sensor data simulation that realistically mimics field noise

## 🎯 Why This Matters

DisasterShield directly aligns with SCAI 2026's theme of **Connected Intelligence** — bringing together smart sensing, edge AI, and remote sensing to build systems with real, localized societal impact.

---

**Solo Developer:** Harsh C. Parmar
**Submitted for:** SCAI 2026 — Project Challenge & Technical Showcase, IEEE SVNIT Surat

**Solo Developer:** Harsh C. Parmar
**Submitted for:** SCAI 2026 — Project Challenge & Technical Showcase, IEEE SVNIT Surat
