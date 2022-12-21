
#------------This File complete project Task 1,2,3--------------------------

import cv2 # used for image and video analysis
import os  # Handling a directory


def imgclsret():
    path = 'images'                         # Import Image folder
    images = []                             # Create empty image list
    classNames = []                         # Create empty className list
    myList = os.listdir(path)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}') # Convert Image file name to perrson name
        images.append(curImg)               # Add All Images using append & for loop method
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)
    return [images,classNames]              # Return images & classNames variables for outer usage