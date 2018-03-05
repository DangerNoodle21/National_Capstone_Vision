### Vision Processing for Robotics

#### Capstone Project for National University

Created: 2/23/2018

Languages: Python, C++ 

This repository holds a computer vision program created for use during robotic competitions. It was developed to detect certain predetermined objects, ascertain certain details about the object and relay that information back to the user. This project was created to fulfill requirements for a Master’s Degree in computer science from National University.

##### Goal for this Project:

- [x] Detect Power Cube Object
- [x] Give the Relative distance to that object
- [x] Stream Video to a viewing location
- [ ] Have Multiple Object Profiles
- [ ] Create Calibration Scheme
- [x] Inegrade Raspi-CV Project into one project

#### This project has 3 Different version due to it development and testing on different environments

1. CV-Only - Only the computer Vision aspect of the project. Will only stream video locally
2. FLASK-I2C-CV - Enables a MJPEG Stream to the local IP at port :5000 with I2C / CV. Meant to run on a Raspberry Pi 3
3. I2C-CV-RASPI - Have the CV and I2C, meant to run on a Raspberry Pi 3

#### Required Python Library’s: 

- imutils
- argparse
- cv2
- numpy
- threading
- time
- smbus2

#### Wiki For this project has the detailed breakdown of how the program works along various diagrams
