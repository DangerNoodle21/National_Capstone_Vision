# Computer Vision for Robotics

## This is a computer vision program written with Python used for object detection. This project was created for the use in robotic competitions such as the First Robotics Competition (FRC).


#### Created:
> 2/23/2018

#### Languages:
> _Python_, _C++_
***


**Features** | _Explanation_
------------------------ | --------------------
**Object Detection** | _Detecting a selected object within a picture using computer processing_
**Calculate Distance to Object** | _Relative distance of object detected to camera calculated using a calibration shot comparison_
**Detection Feedback** | _Created user interface to have detected object identified on video stream and distance easily viewable_
**Serial Communications** | _Send data using I2C protocol and stream processed video to desired destining_
**Object Calibration Scheme** | _Not implemented_

## Usage
To use, simply clone the repository and run the main Python file
```
git clone https://github.com/Shark-Bit/Capstone_FRC-Vision_2018
```

## Command Line Arguments
Various command line arguments are used to employ the listed features and offer more operational flexibility.

` -Arg OPTION`

Example:

`-i2c True`

**Argument** | _Option_ | **Default** | _Explanation_
------------ | -------- | ----------- | --------------
`-i2c` | _Int_ | **0, Off** |  _To Turn On / Off I2C connection output_
`-add` | _Int_ | **0x04** |  _Address for I2C connection Output_
`-ui` | _Int_ | **1, On** |  _To turn on / off output interface elements_
`-t` | _Int_ | **1 (There is only 1 :( )** |  _Target profile selector_



## Required Python Library’s: 
Listed libraries may be installed using Python install PIP. Usage is as follows:
```python
pip install *library*
```
- imutils
- numpy
- smbus2

Also needed for this project is OpenCV. Ins talion varies by system.

- cv2




#### This is a Capstone Project build to fulfill requirements for a Master of Computer Science Degree offered by National University
