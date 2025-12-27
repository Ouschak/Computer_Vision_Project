Focus Tracker – Vision Backend

Focus Tracker is a Python backend prototype that uses OpenCV and MediaPipe
to detect whether a user is looking at the screen in real time.

This repository contains only the vision backend.
No UI, no window tracking, no productivity logic beyond vision signals.

What This Backend Does

Opens the system camera

Detects face landmarks using MediaPipe

Produces a boolean attention signal:

looking_raw – direct vision signal

looking_proxy – debounced, stable signal

Runs continuously until stopped

Designed to be imported and extended by higher-level systems

This backend does not:

Save camera frames

Perform productivity decisions

Block applications

Upload data anywhere

Tech Stack

Python 3.13

OpenCV

MediaPipe

NumPy

Tested on Fedora Linux.

Project Structure
backend/
├── app/            # Entry point
├── trackers/       # Camera and vision tracking logic
├── vision/         # Vision helpers
models/             # MediaPipe models

Setup (First Time)

Clone the repository:

git clone https://github.com/<your-username>/focus-tracker.git
cd focus-tracker


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Sanity check:

python -c "import cv2, mediapipe, numpy; print('ok')"

Run the Vision Backend (Important)

⚠️ Do NOT run files directly

The backend must be run as a module from the project root so Python imports
resolve correctly.

python -m backend.app.vision_lab


This starts:

the camera loop

MediaPipe face detection

real-time vision signal generation

Output

The backend continuously updates internal vision signals such as:

face detected

looking away

stable attention state after debouncing

(Exact output format may evolve as the backend is extended.)

Status

This project is an early-stage vision backend prototype intended as a
foundation for higher-level focus or productivity systems.


## Logging

The application writes logs to `app.log`.

### Log rotation (Linux)

For long-running usage, log rotation is recommended.
A sample `logrotate` configuration is provided in:


To enable it on Fedora/Linux:

sudo cp config/log_rotate/ai-focus.conf /etc/log_rotate.d/ai-focus

