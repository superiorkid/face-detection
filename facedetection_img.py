import cv2

# load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# read the input image
# img = cv2.imread('img-example/example1.jpg')
# img = cv2.imread('img-example/example2.jpg')
img = cv2.imread('img-example/example3.jpg')

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# draw rectangle aroud the faces
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# display the output
cv2.imshow('img', img)
cv2.waitKey()