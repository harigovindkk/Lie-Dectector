# the code is explained here: https://youtu.be/Eex4zBc9r7Y
import os
import cv2
import numpy as np


def capt():
	
	ab=open("config.txt", 'r')
	configlist=ab.readlines()
	print(configlist)
	filenum=configlist[0]
	cwd=os.getcwd()
	try:
		os.mkdir("user "+str(int(configlist[1])))
	except:
		pass
	FILE_OUTPUT = cwd+"/user "+str(int(configlist[1]))+"/output"+filenum+".avi"
	print(FILE_OUTPUT)
	configlist[0]=int(configlist[0])+1
	configlist[0]=str(configlist[0])+"\n"
	print(configlist)
	ab.close()
	ab=open("config.txt", 'w')
	ab.writelines(configlist)
	ab.close()

# Checks and deletes the output file
# You cant have a existing file or it will through an error
	if os.path.isfile(FILE_OUTPUT):
    		os.remove(FILE_OUTPUT)

# Playing video from file:
# cap = cv2.VideoCapture('vtest.avi')
# Capturing video from webcam:
	cap = cv2.VideoCapture(0)

	currentFrame = 0

# Get current width of frame
	width = cap.get(3)   # float
# Get current height of frame
	height = cap.get(4) # float


# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter(FILE_OUTPUT,fourcc, 20.0, (int(width),int(height)))

# while(True):
	while(cap.isOpened()):
    # Capture frame-by-frame
	    ret, frame = cap.read()

	    if ret == True:
        # Handles the mirroring of the current frame
	        frame = cv2.flip(frame,1)

        # Saves for video
	        out.write(frame)

        # Display the resulting frame
	        cv2.imshow('frame',frame)
	    else:
	        break
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

    # To stop duplicate images
	    currentFrame += 1

# When everything done, release the capture
	cap.release()
	out.release()
	cv2.destroyAllWindows()

capt()
