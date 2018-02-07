import numpy as np
import cv2
import os

class SimpleDatasetLoader:
	def __init__(self, preprocessors=None):
		# store the image preprocessor
		self.preprocessors = preprocessors

		# if the preprocessors are None, initialize them as an
		# empty list
		if self.preprocessors is None:
			self.preprocessors = []

	def load(self, imagePaths, verbose=-1):
		# initialize the list of features and labels
		data = []
		labels = []

        # Loop over the input imaages

        for (i, imagePath) in enumerate(imagePaths):

            # Load image and extract the class label assuming
            # that our path ahas the following formate:
            # /path/to/dataSet/{clss}/{image}.jpg

            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]
                        
