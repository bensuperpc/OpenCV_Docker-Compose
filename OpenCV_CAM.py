import numpy as np
import cv2
import os

print(os.environ.get('CAMERA'))
cap = cv2.VideoCapture(os.environ.get('CAMERA'))

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
