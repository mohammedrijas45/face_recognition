import cv2                 # used for image and video analysis
import numpy as np         # mathematical operations on arrays
import face_recognition    # Captures, analyzes, and compares patterns based on the person's facial details
import markname            # Import markname.py file
import findencoding        # Import findencoding.py file
import imgimport           # Import imgimport.py file


def faceframe():
    t = imgimport.imgclsret()               # import one of the variable to two returned variable using list method
    encodeListKnown = findencoding.findEncodings(t[0])    #import all encoding list data in to encodeListKnown variable
    cap = cv2.VideoCapture(0)       # Open a system camera
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25) # Rezize image
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)    # Color Convert by frame
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        for encodeFaces,faceLoc in zip (encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFaces)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFaces)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = t[1][matchIndex].upper()
                print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markname.markatt(name)       # Write a frame over camera
        cv2.imshow('Webcam',img)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # When press a Q Key intrepet a all program
            break