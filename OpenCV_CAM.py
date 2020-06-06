import numpy as np
import cv2
import os

cap = cv2.VideoCapture(os.environ.get('VIDEO'))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter('/save/output.avi', fourcc, 20.0, (640, 480))

save_video = False

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    if k == ord('s'):
        #cv2.imwrite('/save/img.png', frame)
        if save_video == True:
            save_video = False
        else:
            save_video = True
    if save_video == True:
        video_writer.write(frame)


cap.release()
video_writer.release()
cv2.destroyAllWindows()
