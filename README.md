### Vision Processing for Robotics

#### Capstone Project for a Master of Computer Science Degree offered by National University

Created: 2/23/2018

Languages: Python, C++ 

This repository holds a computer vision program created for use during robotic competitions. It was developed to detect certain predetermined objects, ascertain certain details about the object and relay that information back to the user. This project was created to fulfill requirements for a Master’s Degree in computer science from National University.

##### Goal for this Project:

- [x] Detect predetermined objec 
- [x] Calculate relaive distance from detected object to camera
- [x] Stream video to an external location
- [x] Integrate all features into one program
- [ ] Have multiple object profiles
- [ ] Create object profile calibration scheme


#### This project has 2 versions, each stored on its own branch

1. Master Brnach - CV-Build - The main computer vision program which is now compadible with windows / linux, while still support I2C functions
2. PreformanceTesting_Flask - Trying to integrate FLASK streaming while working on preformance enhancments and such. 

#### To use, simply clone this repository and run the main file from the commmand line:

```
git clone https://github.com/Shark-Bit/Capstone_FRC-Vision_2018
```

#### Required Python Library’s: 

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


### Command Line Agrguments

This program uses vairious command line arguments to employ the various features. See below to about how employ the various features of the program. The default state of the program will run with no agruments given and only run on the local machine.






#### Wiki For this project has a detailed breakdown of this project. It is currently being populated
