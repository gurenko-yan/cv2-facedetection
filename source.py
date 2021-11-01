try:
    import cv2
except ModuleNotFoundError:
    print("File source.py can't be started.\nCause: ModuleNotFoundError")

# init picture path
picpath = input("Please, input path of picture: ")
pic = cv2.imread(picpath)

# init haarcascade
haarcascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# change picture color to gray
graypic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

# init list with found faces
facelist = haarcascade.detectMultiScale(graypic, 1.1, 19)

# print list with faces
print("Detected faces: ", len(facelist), "(Number of detected faces maybe is not correct!)")

# marking faces in a picture
# x - facelist[][0]
# y - facelist[][1]
# w - facelist[][2]
# h - facelist[][3]
for (x, y, w, h) in facelist:
    cv2.rectangle(pic, (x, y), (x+w, y+h), (0, 255, 0), 2)

# show result
cv2.imshow("result", pic)
cv2.waitKey(None)
