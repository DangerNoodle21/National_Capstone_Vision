# Computer Vision for Robotics

#### Created:
> 2/23/2018

#### Languages:
> _Python_, _C++_
***


**Goals for this Project** | _Explanation_
------------------------ | --------------------
**Process image to detect object** | _Detecting a selected object within a picture using computer processing_
**Calculate Distance to Object** | _Relative distance of object detected to camera calculated using a calibration shot comparison_
**Enable Detecting Feedback** | _Created user interface to have detected object identified on video stream and distance easily viewable_
**Enable Serial Communications** | _Send data using I2C protocol and stream processed video to desired destining_
**Combine Features** | _Had multiple projects, combined them into one. Comparable with Linux, Mac and Window Operating systems_
**Create Object Profile Calibration Scheme** | _Not implemented_

## Usage
To use, simply clone the repository and run the main Python file
```
git clone https://github.com/Shark-Bit/Capstone_FRC-Vision_2018
```

## Command Line Arguments
This program uses various command line arguments to employ the various features. See below to about how employ the various features of the program. The default state of the program will run with no arguments given and only run on the local machine.

` -Arg OPTION`

Example:

`-i2c True`

**Argument** | _Option_ | **Default** | _Explanation_
------------ | -------- | ----------- | --------------
`-i2c` | _Bool_ | **False** |  _To Turn On / Off I2C connection output_
`-add` | _Int_ | **0x04** |  _Address for I2C connection Output_
`-UI` | _Bool_ | **True** |  _To turn on / off output interface elements_
`-t` | _Int_ | **1** |  _Target profile selector_



## Required Python Library’s: 
Listed libraries may be installed using Python install PIP. Usage is as follows:
```python
pip install *library*
```
- imutils
- argparse
- numpy
- threading
- smbus2

Also needed for this project is OpenCV. Ins talion varies by system.

- cv2

## Branches

1. Master - The main computer vision program. Compatible with windows / Linux while still supporting I2C functions

2. PreformanceTesting_Flask - Trying to integrate FLASK streaming while working on performance enhancements and such. 






#### This is a Capstone Project build to fulfill requirements for a Master of Computer Science Degree offered by National University
