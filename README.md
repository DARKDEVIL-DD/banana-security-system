# Useless3.0
# 🍌 Anti-Theft Banana Security System

## Basic Details

### Team Name: [Cltrl ALT Defeat]

### Team Members

* Team Lead: [Ann Sebatina Sibichen] - [CARMEL COLLEGE OF ENGINEERING AND TECHNOLOGY ]
* Member 2: [Irshad N] - [CARMEL COLLEGE OF ENGINEERING AND TECHNOLOGY ]

## Project Description

The Anti-Theft Banana Security System is an AI-powered security system designed to protect one of the world's most valuable assets — a banana. 🍌

Using Python, OpenCV, and YOLO-based object detection, the system monitors a banana through a camera and detects when it disappears. If the banana remains undetected for a specific period, the system declares a **BANANA THEFT 🚨** and activates an alarm.

## The Problem (that doesn't exist)

People have security systems for houses, cars, shops, phones, and even bicycles.

But what about bananas?

A banana left unattended is exposed to serious risks such as:

* 🍌 Unauthorized banana consumption
* 🍌 Banana disappearance
* 🍌 Suspicious human activity near the banana
* 🍌 Unexplained banana relocation
* 🍌 Extremely dangerous banana theft

Clearly, the world has been ignoring this critical security problem.

## The Solution (that nobody asked for)

We developed an AI-powered surveillance system that continuously watches over a banana.

The camera captures the surroundings and the AI checks whether a banana is present. If the banana disappears for a predefined period, the system assumes that a theft has occurred and raises an alarm.

The system provides a completely unnecessary but technically impressive solution to the world's most important banana-related security problem.

## Technical Details

### Technologies/Components Used

### For Software

* **Language:** Python
* **Computer Vision:** OpenCV
* **AI/Object Detection:** YOLO
* **Numerical Processing:** NumPy
* **Development Environment:** Visual Studio Code
* **Camera:** Laptop webcam / Mobile camera
* **Operating System:** Windows

### For Hardware

No dedicated electronic hardware is required.

The project uses:

* Laptop
* Built-in mobile camera
* Banana 🍌

## Implementation

### For Software

The system follows the following process:

1. The camera captures live video.
2. OpenCV reads the camera frames.
3. YOLO processes each frame.
4. The AI model checks whether a banana is detected.
5. If a banana is detected, the system displays **BANANA SAFE**.
6. If the banana disappears, a timer is started.
7. If the banana remains undetected for the defined time, theft is detected.
8. The system displays a theft warning.
9. An alarm is activated.
10. The theft attempt is recorded/count is increased.
11. When the banana returns, the system can be reset to the safe state.

### Detection Logic

```text
                START
                  ↓
          Start Camera
                  ↓
        Capture Video Frame
                  ↓
          YOLO Object Detection
                  ↓
          Is Banana Detected?
             ↙          ↘
           YES           NO
            ↓             ↓
      BANANA SAFE     Start Timer
            ↓             ↓
       Continue       Wait 3 Seconds
       Monitoring          ↓
                       Banana Back?
                       ↙       ↘
                     YES        NO
                      ↓          ↓
                 BANANA SAFE   THEFT 🚨
                                  ↓
                           Activate Alarm
                                     
```

# Installation

### 1. Install Python

Download and install Python from:

https://www.python.org/

During installation, enable:

```text
Add Python to PATH
```

### 2. Clone the Repository

```bash
git clone https://github.com/[your-username]/[your-repository].git
```

Move into the project folder:

```bash
cd Anti-Theft-Banana-Security-System
```

### 3. Install Required Libraries

Install OpenCV:

```bash
pip install opencv-python
```

Install NumPy:

```bash
pip install numpy
```

Install Ultralytics YOLO:

```bash
pip install ultralytics
```

### 4. Install All Dependencies

If a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

# Run

Run the main Python program:

```bash
python main.py
```

The camera window will open and the AI will start detecting objects.

Place a banana in front of the camera.

The system should display:

```text
🍌 BANANA SAFE
```

When the banana is removed and remains undetected for the configured time, the system displays:

```text
🚨 BANANA THEFT DETECTED 🚨
```

Press:

```text
Q
```

to close the camera window.

### Project Documentation

## Screenshots

### Screenshot 1 — Camera Monitoring
![alt text](image.png)
![alt text](<Screenshot (137).png>)

*Live camera feed showing the banana under continuous AI-based monitoring.*

### Screenshot 2 — Banana Detection

![alt text](<Screenshot (138).png>)

*YOLO detects the banana and displays the detected object with its confidence level.*

### Screenshot 3 — Theft Detection

![alt text](<Screenshot (139).png>)

*The system detects that the banana has disappeared and displays the Banana Theft Alert.*

## Diagrams

### System Workflow

![Workflow](diagrams/workflow.png)

*Workflow showing the complete process from camera input to banana detection and theft alert.*

### System Architecture

```text
┌──────────────────────┐
│   Mobile/Laptop      │
│       Camera         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│       OpenCV         │
│   Video Processing   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│       YOLO AI        │
│  Object Detection    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Banana Detected?     │
└──────────┬───────────┘
       YES ↓       ↓ NO
┌──────────────┐   ┌───────────────┐
│ BANANA SAFE  │   │ Start Timer   │
│      ✅      │   └───────┬───────┘
└──────────────┘           ↓
                    ┌───────────────┐
                    │ Missing for   │
                    │ 3+ seconds?   │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │ THEFT ALERT   │
                    │      🚨       │
                    └───────────────┘
```

### Project Demo

## Video

https://drive.google.com/file/d/1avasJ9ClkCm3gdeJ-2wdZMOFMiyIXpV4/view?usp=sharing

*The demonstration video shows the AI detecting the banana, monitoring its presence, detecting its disappearance, and triggering the Banana Theft Alert.*

## Additional Demos

* [GitHub Repository](Add GitHub repository link)
* [Demo Video](Add demo video link)
* [Project Presentation](Add presentation link, if available)

## Team Contributions

* **[Name 1]:** Project planning, Python programming, AI/object detection implementation, and integration.
* **[Name 2]:** OpenCV camera implementation, testing, debugging, and documentation.
* **[Name 3]:** User interface, project presentation, demonstration, and GitHub documentation.

---

## 🍌 Why This Project?

Because apparently, humanity has successfully developed advanced security systems for everything except bananas.

**Problem:** Banana theft.

**Solution:** Artificial Intelligence.

**Necessity:** Absolutely none.

**Technology:** Surprisingly real.

**Banana:** Hopefully safe. 🍌🔐

---

## Future Improvements

Possible future improvements include:

* 📱 Mobile phone camera integration
* 🔊 Advanced alarm system
* 📸 Automatic thief snapshot
* 👤 Person detection
* 📊 Theft history dashboard
* ⏱️ Customizable detection timer
* 🌐 Web-based monitoring
* 📲 Mobile notifications
* 🍌 Banana identification and tracking
* 🤖 More advanced AI-based security features

## Conclusion

The Anti-Theft Banana Security System demonstrates how modern computer vision and artificial intelligence can be applied to even the most unnecessary problems.

While protecting a banana may not be a real-world necessity, the project demonstrates practical concepts such as real-time video processing, object detection, AI integration, event detection, and automated alerts.