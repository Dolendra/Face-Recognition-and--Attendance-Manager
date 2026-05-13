import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'dataset'
images=[]
classNames=[]
MyList = os.listdir(path)
print(MyList)

for cl in MyList:
    curImg =cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0]) 
print(classNames)

def findEncodings(images):
    encodeList=[]
    for img  in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList



# the below step ia s to mark the attendence this is the last step of the project

def markAttendence(name):
    # we want to store the name, time and date, so for time and date we need a library
    with open('attendance.csv','r+') as f:
        myDataList=f.readlines()
        nameList = []
        # print(myDataList)
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


# markAttendence('elon')   # whenever we detect a face we must call this function and give it the name




encodeListKnown = findEncodings(images)
print(len(encodeListKnown))
print('Encoding completed')

cap = cv2.VideoCapture(0)    # 0 as our id

while True :
    success,img = cap.read()
    imgsmall = cv2.resize(img,(0,0),None,0.25,0.25)   # to make fast we resize and if we want to do that pass that img and if we want pixel (0,0)    , None , scale
    imgsmall = cv2.cvtColor(imgsmall,cv2.COLOR_BGR2RGB)
    # there may be possibility of multiple faces in webcam so to avoid it we must find the locarions of the faces
    facesCurFrame = face_recognition.face_locations(imgsmall)
    encodesCurFrame = face_recognition.face_encodings(imgsmall,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDist = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDist)     # starts giving you the distance for all images and which is having the least distance is you
        matchIndex = np.argmin(faceDist)


        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc        # we dont get the rectange to our face because we performed these oprations after scaling to 0.25 so we must multiply it
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)    # img , coordinates , color , thickness
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendence(name)

    # we must create the bound box to see image

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)








# imgelon = face_recognition.load_image_file('dataset/elon.webp')
# imgtest = face_recognition.load_image_file('dataset/billgates.jpg')

# imgelon = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
# imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)





# faceloc = face_recognition.face_locations(imgelon)[0]
# encodeElon = face_recognition.face_encodings(imgelon)[0]
# cv2.rectangle(imgelon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
 
# # print(faceloc)   # gets dimensions of face

# facelocTest = face_recognition.face_locations(imgtest)[0]
# encodeTest = face_recognition.face_encodings(imgtest)[0]
# cv2.rectangle(imgtest,(facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(255,0,255),2)


# # comparing the faces  linear svm is used at backend whether they matched or not 

# results = face_recognition.compare_faces([encodeElon],encodeTest)     # first argument is list but not the second

# # to find the distance between faces (differentiate)
# faceDis = face_recognition.face_distance([encodeElon],encodeTest)