# Focus Tracker Backend

Focus Tracker is a Python backend that uses OpenCV and MediaPipe to compute a `looking_proxy` signal based on camera input.  
It is part of a larger desktop productivity monitoring system.

This backend is **responsible only for the vision logic and signals**.  
Frontend and UI are separate and not included here.

---

## 🧠 What This Backend Does

- Opens the camera using OpenCV
- Detects a face and landmarks using MediaPipe
- Computes a simple proxy for “user looking at the screen”
- Exposes structured signals used by the rest of the application

---

## 🚀 Requirements

- Fedora Linux (X11 recommended)
- Python 3.10+
- Camera access
- X11 session (for display and window tracking)

---

## 📦 Setup (Backend Only)

1. Create a virtual environment:

```bash
python3 -m venv venv
````

2. Activate it:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> This installs OpenCV, MediaPipe, NumPy and other required packages.

---

## ▶️ Running the Vision Module

Run the vision sandbox:

```bash
python -m backend.app
```

or

```bash
python -m backend.app
```

This ensures Python sees your `backend` package correctly.

---

## 🧪 How It Works (High Level)

1. **OpenCV** opens the camera.
2. **MediaPipe FaceMesh** extracts facial landmarks.
3. A simple rule computes `looking_proxy`:

   * Head roughly centered → `True`
   * Not centered → `False`

This output can be used by a controller or UI module.

---

## 📁 Backend Structure

```
backend/
├── __init__.py
├── app.py
├── trackers/
│   ├── __init__.py
│   ├── camera.py
│   └── vision.py
└── utils/
    └── ...
```

Only backend logic is included here. UI and frontend live outside this repository.

