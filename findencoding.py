import cv2                  # used for image and video analysis
import face_recognition     # Analyzes, and compares patterns based on the person's facial details.

def findEncodings(images):
    encodeLists = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)        # Converted to color image frame to black & white
        encode = face_recognition.face_encodings(img)[0] # encode a frame
        encodeLists.append(encode)
    return encodeLists                                   #return encodeList for outer usage