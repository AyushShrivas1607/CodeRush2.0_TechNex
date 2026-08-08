# 🚀 Space Mission Operations Automator

> **CodeRush 2.0 | Team Project Repository**  
> **SDG-03** — Space Mission Operations Automator  
> **Problem Statement:** *Simulation-first mission planning and telemetry*

---

## 📌 Project Information

- **Team Name:** `TechNex`
- **Project Title:** **Space Mission Operations Automator**
- **Track / Theme:** **SDG-03**
- **Domain:** Space Technology • Mission Operations • Simulation • Telemetry

---

## 🎯 Project Overview

**Space Mission Operations Automator** is a simulation-first platform designed to simplify and automate important space mission operations.

The system provides a centralized environment for **mission planning, mission simulation, telemetry monitoring, satellite tracking, AI/ML-based analysis, alerts, analytics, and report generation**.

The simulation-first approach allows mission scenarios and operational conditions to be tested in a controlled environment before real-world execution.

### Core Objectives

- 🛰️ Simplify mission planning and configuration.
- 🧪 Simulate mission scenarios before execution.
- 📡 Monitor mission telemetry.
- 🌍 Track satellite and mission status.
- 🤖 Apply AI/ML for intelligent image/data analysis.
- 📊 Visualize mission and telemetry analytics.
- 🚨 Detect and display abnormal conditions.
- 📄 Generate mission reports.
- 🔐 Secure access using 2-Step Verification (2SV).

---

## ✨ Key Features

### 🔐 Authentication & Security
- User login and registration.
- **2SV Verification API** for additional authentication security.
- Protected mission-operation features.

### 🛰️ Mission Planning
- Create and configure missions.
- Define mission parameters.
- Configure mission objectives.
- Validate mission configuration before simulation.

### 🧪 Mission Simulation
- Simulation-first mission workflow.
- Mission countdown and status tracking.
- Orbit and mission-state visualization.
- Simulated telemetry.
- Mission event and alert monitoring.

### 📡 Telemetry Monitoring
- Mission telemetry dashboard.
- Battery, fuel, altitude, velocity, and status monitoring.
- Telemetry charts and trend visualization.

### 🤖 AI/ML Analysis
- **MobileNetV2** for lightweight image classification/feature extraction.
- **CNN model** for image-based analysis and classification.
- **NumPy** for numerical processing.
- **Pandas** for dataset and telemetry processing.
- AI/ML outputs can support mission analysis and alerts.

### 🌍 Satellite Tracking
- Satellite status monitoring.
- Mission/satellite information.
- Tracking-oriented visualization.

### 📊 Analytics & Reports
- Telemetry trend analysis.
- Mission performance indicators.
- AI/ML analysis results.
- Mission summaries and reports.

---

## 🛠️ Technical Stack

### Backend

- **Python**
- **AI/ML**
- **MobileNetV2**
- **CNN (Convolutional Neural Network)**
- **NumPy**
- **Pandas**
- **2SV Verification API**

### Frontend

- **HTML5**
- **Tailwind CSS**
- Responsive dashboard UI
- Mission simulation interface
- Telemetry and analytics views

### AI/ML Pipeline

```text
Input Image / Mission Data
          ↓
   NumPy + Pandas
          ↓
 Image/Data Preprocessing
          ↓
   CNN / MobileNetV2
          ↓
    AI/ML Prediction
          ↓
 Mission Analysis / Alert
          ↓
 Dashboard & Reports
```

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │         User            │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   HTML + Tailwind CSS   │
                    │      Web Interface      │
                    └────────────┬────────────┘
                                 │
                         2SV Verification API
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Python Backend      │
                    └────────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
        Mission Planning   Simulation Engine   Telemetry
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       AI / ML Layer     │
                    │ MobileNetV2 + CNN       │
                    │ NumPy + Pandas          │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ Analytics / Alerts /    │
                    │ Reports / Visualization │
                    └─────────────────────────┘
```

---

## 📂 Project Structure

```text
space-mission-operations-automator/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── models/
│   │   ├── mobilenetv2_model.py
│   │   └── cnn_model.py
│   │
│   ├── services/
│   │   ├── mission_service.py
│   │   ├── telemetry_service.py
│   │   ├── ai_service.py
│   │   └── verification_service.py
│   │
│   ├── utils/
│   │   ├── preprocessing.py
│   │   └── data_processing.py
│   │
│   └── data/
│       ├── datasets/
│       └── telemetry/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── mission-planner.html
│   ├── mission-simulation.html
│   ├── telemetry.html
│   ├── satellite-tracking.html
│   ├── analytics.html
│   ├── reports.html
│   ├── settings.html
│   └── assets/
│       ├── css/
│       ├── js/
│       └── images/
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🚀 Setup and Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create a Python Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create `.env` from `.env.example`.

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

**Windows CMD:**

```cmd
copy .env.example .env
```

**Git Bash / macOS / Linux:**

```bash
cp .env.example .env
```

Example:

```env
VERIFICATION_API_URL=<YOUR_2SV_VERIFICATION_API>
MODEL_PATH=<YOUR_MODEL_PATH>
```

> ⚠️ Never commit API keys, tokens, or private credentials to GitHub.

### 5. Start the Python Backend

For a Flask-style backend:

```bash
python app.py
```

For a FastAPI-style backend:

```bash
uvicorn app:app --reload
```

Use the command matching your implementation.

### 6. Run the HTML + Tailwind Frontend

```bash
python -m http.server 5500
```

Then open:

```text
http://localhost:5500
```

---

## 🔄 Mission Workflow

```text
Login / Register
       ↓
2SV Verification
       ↓
Mission Dashboard
       ↓
Create Mission
       ↓
Configure Mission Parameters
       ↓
Validate Mission
       ↓
Start Simulation
       ↓
Mission Countdown
       ↓
Orbit / Mission Simulation
       ↓
Telemetry Monitoring
       ↓
AI/ML Analysis
       ↓
Satellite Tracking
       ↓
Analytics & Alerts
       ↓
Generate Mission Report
```

---

## 🤖 AI/ML Capabilities

### MobileNetV2

**MobileNetV2** is used as a lightweight deep-learning model for efficient image classification and feature extraction. It is suitable for applications where computational efficiency is important.

### CNN Model

A **Convolutional Neural Network (CNN)** can be used for domain-specific image classification, feature extraction, and visual analysis tasks.

### NumPy

**NumPy** supports numerical operations, matrix calculations, preprocessing, and transformation of ML data.

### Pandas

**Pandas** is used to clean, organize, transform, and analyze telemetry, mission, and training datasets.

### 2SV Verification API

The **Two-Step Verification (2SV) API** provides an additional authentication layer to improve application security.

---

## 📊 Telemetry Parameters

| Parameter | Purpose |
|---|---|
| 🪫 Battery | Monitor spacecraft power status |
| ⛽ Fuel | Track remaining fuel |
| 🛰️ Altitude | Monitor orbital altitude |
| 🚀 Velocity | Track spacecraft velocity |
| 📡 Mission Status | Display current mission state |
| ⚠️ Alerts | Identify abnormal or critical conditions |

---

## 🎨 UI / UX Highlights

- Modern space-themed interface.
- HTML5 + Tailwind CSS responsive design.
- Mission-control dashboard.
- Interactive telemetry cards and charts.
- Simulation status and countdown.
- Satellite tracking interface.
- AI/ML analysis results.
- Clear alerts and mission status indicators.

---

## 🔮 Future Enhancements

- AI-based anomaly detection.
- Predictive telemetry analysis.
- Real satellite data integration.
- Advanced orbital calculations.
- Automated mission scheduling.
- WebSocket-based live telemetry.
- Role-based access control.
- Cloud deployment.
- 3D spacecraft/orbit visualization.
- Automated emergency-response recommendations.

---

## 👥 Team

| Member | Role |
|---|---|
| `Mrunmayi Joshi` | `Backend` |
| `Disha Lohoti` | `AI/ML` |
| `Anchal Yadav` | `Frontend` |
| `Ayush Shrivas` | `Backend` |
| `Shomesh Gawande` | `Frontend` |

---

## 🏆 CodeRush 2.0

This project is developed as a team project for **CodeRush 2.0**.

**SDG:** SDG-03  
**Project:** **Space Mission Operations Automator**  
**Problem Statement:** *Simulation-first mission planning and telemetry*

---

## 📜 License

This project is developed for educational, hackathon, and demonstration purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
