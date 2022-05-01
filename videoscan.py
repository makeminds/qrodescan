import cv2
import numpy as np
from numpy.core.arrayprint import printoptions
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
start_point = (5, 5)
end_point = (635, 475)
greencolor = (0, 255, 0)
redcolor = (0, 0, 255)
thickness = 5

while True:
    _, frame = cap.read()


    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        code=str(obj.data)
        location1 = "insert address"
        location2 = "insert address"
        url = f"b'https://maps.google.com/local?q={location1},{location2}'"
        if code == url:
            window_text = "Right Address!"
            cv2.putText(frame, window_text, (50, 50), font, 4, (0, 255, 0), 3)            
            cv2.rectangle(frame, start_point, end_point, greencolor, thickness)
        else:
            window_text = "Wrong Address!"
            cv2.putText(frame, window_text, (50, 50), font, 4, (0, 0, 255), 3)
            cv2.rectangle(frame, start_point, end_point, redcolor, thickness)
    
    cv2.imshow("dunnoname.AI - Meer", frame)
        
    key = cv2.waitKey(1)
    if key == 27:
        break
    


