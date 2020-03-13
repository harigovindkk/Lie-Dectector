import cv2
import sys
import numpy as np
from timeit import default_timer as timer

start=timer()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
c=0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        k=1
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            k=0
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
        if k==1:
            sys.stdout.write('\a')
            sys.stdout.flush()
            out="You've blinked ",c," times"
            c=c+1
            #print (out)
    
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff 
    if k==ord('q'):
        break
f=open("result.txt","a+")
count=(int)(c)
f.write("\n\nEye Blink Count Result:-\nTheory :- The average eye blinking count of a normal person : 12-15 per minute.")
f.write("\nThe total eye blink count calculated : ")
f.write(str(count))
end=timer()
f.write("\nThe total time analysed in second : ")
sec=(int)(end-start)
f.write((str)(sec))
val=(int)((count*60)/sec)
f.write("\nThe average eye blinking count per minute calculated :  ")
f.write((str)(val))
if(val<12 or val >15):
    f.write("\nTherefore, CHANCE OF LIE")
else :
    f.write("\nTherefore, No abnormalities found")

cap.release()
cv2.destroyAllWindows()
