# Computer Vision for Robotics

#### Created:
> 2/23/2018

#### Languages:
> _Python_, _C++_
***
***





Goals for this Project | Explanation
---------------------- | --------------------
**Process image to detect object** | Dection an object from a video stream after a vision profile of the object has build and calibrated_
**Calculte Distance to Object** | _Relative distance of object detected to camera calculated using a calibraion shot comparison_
**Enable Detectin Feedback** | _Created user intefaace to have detected object identifed on video stream and distance easily viewable_
**Enable Serial Communications** | _Send data using I2C protocal and stream processed video to desired destion_
**Combine Features** | _Had multiple projects, combined them into one. Compadable with Linux, Mac and Window Operating systems_
**Create Object Profile Calibration Scheme** | _Not implemented_

## Usage
To use, simply clone the repository and run the main Python file
```
git clone https://github.com/Shark-Bit/Capstone_FRC-Vision_2018
```

## Command Line Agrguments
This program uses vairious command line arguments to employ the various features. See below to about how employ the various features of the program. The default state of the program will run with no agruments given and only run on the local machine.




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

## Branches

1. Master - The main computer vision program. Compadible with windows / linux while still supporting I2C functions

2. PreformanceTesting_Flask - Trying to integrate FLASK streaming while working on preformance enhancments and such. 










#### This is a Capstone Project build to fulfill requriments for a Master of Computer Science Degree offered by National University
