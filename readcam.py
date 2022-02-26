try:
    import cv2
except ModuleNotFoundError:
    print("File source.py can't be started.\nCause: ModuleNotFoundError")

haarcascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

cam.set(3, 512)
cam.set(4, 512)

while True:
    success, pic = cam.read()

    graypic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

    facelist = haarcascade.detectMultiScale(graypic, 1.1, 5)
    
    print("Detected faces: ", len(facelist), "(Number of detected faces maybe not correct!)")

    # x - facelist[][0]
    # y - facelist[][1]
    # w - facelist[][2]
    # h - facelist[][3]
    for (x, y, w, h) in facelist:
        cv2.rectangle(pic, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("result", pic)
    cv2.waitKey(1)
