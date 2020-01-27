import cv2

faceCascadeFrontal = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
facecascadeProfile = cv2.CascadeClassifier('haarcascade_profileface.xml')

additive = 5 # Добавка
direction = ""
previous_face = [[0,0,0,0]] # Начальное положение

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

        #Определение направления
        if faces is not ():
            if previous_face[0][0] + additive < faces[0][0]:
                direction += " Left"
            if previous_face[0][0] - additive > faces[0][0]:
                direction += " Right"
            if (previous_face[0][0] + previous_face[0][2] + additive) < (faces[0][0] + faces[0][2]) and (
                    previous_face[0][1] + previous_face[0][3] + additive) < (faces[0][1] + faces[0][3]):
                direction += " Bigger"
            if (previous_face[0][0] + previous_face[0][2] - additive) > (faces[0][0] + faces[0][2]) and (
                    previous_face[0][1] + previous_face[0][3] - additive) > (faces[0][1] + faces[0][3]):
                direction += " Smaller"
            previous_face = faces

        print(direction)
        cv2.putText(img, direction, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    resized_img = cv2.resize(img, (1000, 700))
    cv2.imshow('video', resized_img)
    direction = ""
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()