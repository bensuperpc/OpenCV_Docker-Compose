import numpy as np
import cv2
import os

print(os.environ.get('CAMERA'))
cap = cv2.VideoCapture(os.environ.get('CAMERA'))

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    if k == ord('s'):
        cv2.imwrite('/save/img.png', frame) 

cap.release()
cv2.destroyAllWindows()
