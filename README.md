## Computer Vision for Robotics


**Created: 2/23/2018**

**Languages: Python, C++** 

**Features:**
- _Object detection_
- _Relative distance calculation from object to camera_
- _serial communications_


## Goals for this Project:
- [x] Detect predetermined objec 
- [x] Calculate relaive distance from detected object to camera
- [x] Stream video to an external location
- [x] Integrate all features into one program
- [ ] Have multiple object profiles
- [ ] Create object profile calibration scheme


## Branches

1. Master - The main computer vision program. Compadible with windows / linux while still supporting I2C functions

2. PreformanceTesting_Flask - Trying to integrate FLASK streaming while working on preformance enhancments and such. 



## Usage
To use, simply clone the repository and run the main Python file
```
git clone https://github.com/Shark-Bit/Capstone_FRC-Vision_2018
```

## Required Python Library’s: 
All of these listed library may be installed using Python instll PIP. Usage is as follows:
```python
pip install *library*
```
- imutils
- argparse
- numpy
- threading
- smbus2

Also needed for this project is OpenCV. Instalion varies by system.

- cv2


## Command Line Agrguments
This program uses vairious command line arguments to employ the various features. See below to about how employ the various features of the program. The default state of the program will run with no agruments given and only run on the local machine.





#### Capstone Project for a Master of Computer Science Degree offered by National University
#### Wiki For this project has a detailed breakdown of this project. It is currently being populated
