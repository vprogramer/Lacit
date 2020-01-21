import cv2

faceCascadeFrontal = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
facecascadeProfile = cv2.CascadeClassifier('haarcascade_profileface.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascadeFrontal.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
    if faces is ():
        faces = facecascadeProfile.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('video', img)

 #   if previous_face[0] < x and previous_face[1] < y and previous_face[2] < w and previous_face[3] < h:
  #      print("Lower")
    #cv2.putText(img, direction, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if faces is not ():
        previous_face = faces
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()