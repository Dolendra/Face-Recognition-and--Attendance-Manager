# # cmake  dlib- 19.18  face-recognition  opencv-python  numpy   -- install all these dependencies 
# # next step is to import them

# # #1. Create a Virtual Environment (Recommended)
# # It's best to use a virtual environment to manage dependencies.

# # For Windows (Command Prompt or PowerShell)

# # python -m venv venv
# # Activate it:

# # Command Prompt: venv\Scripts\activate
# # PowerShell: venv\Scripts\Activate.ps1




# # To install OpenCV (`cv2`) in your VS Code environment, follow these steps:

# # ---

# # ### **1. Activate Virtual Environment (If using one)**
# # If you're using a virtual environment (recommended), activate it:

# # #### **Windows (Command Prompt)**
# # ```sh
# # venv\Scripts\activate
# # ```
# # #### **macOS/Linux**
# # ```sh
# # source venv/bin/activate
# # ```

# # ---

# # ### **2. Install OpenCV**
# # Use `pip` to install OpenCV:

# # pip install opencv-python


# # If you need additional OpenCV functionalities like `cv2.imshow()` (which requires GUI support), install:

# # pip install opencv-python-headless


# # For full OpenCV with extra dependencies (e.g., for `cv2.VideoCapture`):

# # pip install opencv-contrib-python




# # ### **3. Verify Installation**
# # Run the following in Python to check if OpenCV is installed correctly:
# # ```python
# # import cv2
# # print(cv2.__version__)
# # ```

# # If you see an output with a version number, OpenCV is installed successfully! 🚀 Let me know if you face any issues.


# # cv2 required to install face-recogintion 


import cv2
import numpy as np
import face_recognition
# print(cv2.__version__)
# print("Face Recognition Library Loaded Successfully!")

imgelon = face_recognition.load_image_file('dataset/elon.webp')
imgtest = face_recognition.load_image_file('dataset/billgates.jpg')


imgelon = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)


# faceloc = face_recognition.face_locations(imgelon)   # if you dont keep [0] here u must use commented part

faceloc = face_recognition.face_locations(imgelon)[0]
encodeElon = face_recognition.face_encodings(imgelon)[0]
cv2.rectangle(imgelon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
# cv2.rectangle(imgelon, (faceloc[0][3], faceloc[0][0]), (faceloc[0][1], faceloc[0][2]), (255, 0, 255), 2)     # this sould be used if [0] is not kept
# print(faceloc)   # gets dimensions of face

facelocTest = face_recognition.face_locations(imgtest)[0]
encodeTest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(255,0,255),2)


# comparing the faces  linear svm is used at backend whether they matched or not 

results = face_recognition.compare_faces([encodeElon],encodeTest)     # first argument is list but not the second

# to find the distance between faces (differentiate)
faceDis = face_recognition.face_distance([encodeElon],encodeTest)
print(results,faceDis)

cv2.putText(imgtest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('Dolendra',imgelon)
cv2.imshow('Manoj Test',imgtest)
cv2.waitKey(0)










# import cv2
# import numpy as np
# import face_recognition
# import os

# # Load images
# img_path1 = 'dataset/manoj/Screenshot 2025-02-15 115234.png'
# img_path2 = 'dataset/manoj/Screenshot 2025-02-15 115216.png'

# if not os.path.exists(img_path1) or not os.path.exists(img_path2):
#     print("One or both images not found!")
# else:
#     imgelon = face_recognition.load_image_file(img_path1)
#     imgtest = face_recognition.load_image_file(img_path2)

#     # Convert to RGB (not grayscale!)
#     imgelon = cv2.cvtColor(imgelon, cv2.COLOR_BGR2RGB)
#     imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)

#     # Detect face
#     faceloc = face_recognition.face_locations(imgelon)
#     if len(faceloc) == 0:
#         print("No face detected in first image!")
#     else:
#         encodeElon = face_recognition.face_encodings(imgelon)[0]
#         cv2.rectangle(imgelon, (faceloc[0][3], faceloc[0][0]), (faceloc[0][1], faceloc[0][2]), (255, 0, 255), 2)

#     # Show images
#     cv2.imshow('Manoj', imgelon)
#     cv2.imshow('Manoj test', imgtest)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
