import cv2
import numpy as np

# load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# capture video from webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened:
  print('Kamera tidak dapat diakses')
  exit()
  
pressQkey = False
while(pressQkey == False):
  # read the frame
  ret, img = cap.read()
  
  if ret == True:
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect the faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 2)
    
    # draw the rectangle around each face
    for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
      
    # display
    cv2.imshow('img', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      pressQkey = True
      break
    

cap.release()
cv2.destroyAllWindows()
      

  
