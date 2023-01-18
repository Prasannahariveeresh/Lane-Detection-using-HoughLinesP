# Lane Detection using HoughLinesP in OpenCV Python
This repository contains the code for a lane detection system implemented using the HoughLinesP function from the OpenCV library in Python. The system is able to detect lane lines in an image with a high level of accuracy.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Prerequisites
You will need to have the following software installed on your machine:

  1. Python 3
  2. OpenCV
  3. Numpy
  4. Matplotlib

You can install these libraries using pip:

  `pip install opencv-python numpy matplotlib`

# Running the code
The code for the lane detection system can be found in the file lane_detection.py. To run the code, simply navigate to the directory containing the file in your terminal and run the following command:

  `python lane_detection.py`

This will open the input image and display the output image with the detected lane lines drawn in green.

# How it works
The lane detection system works by applying the following steps to the input image:

# Convert the image to grayscale
Apply a Gaussian blur to the grayscale image
Use the Canny edge detection algorithm to detect edges in the blurred image
Use the HoughLinesP() function from OpenCV to detect lines in the edge-detected image
Draw the detected lines on the original image

# Conclusion
This repository demonstrates the power of computer vision in solving real-world problems and the ease of use of OpenCV in implementing computer vision tasks in Python. With the help of HoughLinesP function and some image processing techniques, we were able to implement a lane detection system that is able to detect lane lines in an image with a high level of accuracy.

# Author
Prasannahariveeresh J R - [Blog](https://jrprasanna.com) - prassijr@gmail.com

# License
This project is licensed under the MIT License - see the LICENSE.md file for details
