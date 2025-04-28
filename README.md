# Smart Vehicle Traffic Management System Using IoT and Machine Learning 🚦

smart-traffic-management-system/
│
├── README.md                  # Project overview, setup, usage, contributors
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files/folders to ignore by Git
│
├── data/
│   ├── ambulance/              # Training images: ambulances
│   ├── non_ambulance/           # Training images: other vehicles
│   └── test_images/             # Images for testing inference
│
├── model/
│   ├── ambulance_detector_model.h5   # Saved ML model
│   └── tflite_model.tflite            # (Optional) Quantized model for IoT
│
├── iot-device/
│   ├── camera_feed.py          # Code to capture camera feed
│   ├── ambulance_inference.py  # Code to run ML model on IoT device
│   ├── traffic_controller.py   # Code to control traffic lights based on detection
│   └── utils.py                # Helper functions (image processing, etc.)
│
└── simulations/
    ├── traffic_simulation.py   # Simulated congestion scenarios
    └── ambulance_test_case.py  # Simulated ambulance approach test


## Problem Statement
Urban traffic congestion leads to delays, inefficiency, and higher emissions. Our project proposes a smart IoT-based traffic management system integrating real-time data collection and machine learning for dynamic signal control.

## Features
- Real-time Ambulance Detection
- Dynamic Traffic Light Management
- IoT Integration using Raspberry Pi

## Technologies Used
- TensorFlow 2.x
- OpenCV
- Flask (Optional for server)
- Raspberry Pi (or similar IoT hardware)

## Setup
1. Clone the repo
2. Install Python dependencies:  
   `pip install -r requirements.txt`
3. Run IoT device code.
4. Connect to traffic light controller API.

## Team
- Mrinal Nilesh Jani
- Manoj B C
- Karthik Kumar G V

**Guide**: 
