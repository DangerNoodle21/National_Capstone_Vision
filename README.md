# Computer Vision for Robotics

### This is a computer vision program used for basic object recognition. The project was created for the use in robotic competitions such as the First Robotics Competition (FRC) and the fulfillment in the completion of my master’s degree. It uses python / C++ to recognize a predetermined object (a yellow box).

#### For program specifics, please see the [Wiki](https://github.com/Shark-Bit/Capstone_FRC-Vision_2018/wiki)

#### Created:
> 2/23/2018

#### Languages:
> _Python 3_, _C++_
***

## Project Features

**Function** | _Explanation_
------------------------ | --------------------
**Object Detection** | _Detecting a selected object within a picture using image processing_
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

`-i2c 1`

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

Also needed for this project is [OpenCV](https://opencv.org/).

- cv2


## Status of Project
This was a Capstone Project build to fulfill requirements for a Master of Computer Science Degree offered by National University. As of right now, it is being used as resource for the various parties is was built for. Minor features will be implemented as well as performance experiments regarding multi-threading. These experiments will be merged into the main branch if performance it the future*.
