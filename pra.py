from cvzone.ClassificationModule import Classifier
import cvzone
import cv2
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os


fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="select img file ",filetypes=(("JPG file","*.jpg"),("PNG file ","*.png"),("All Files","*.*")))
 #cap = cv2.VideoCapture(1)#for ext camera
maskClassifier = Classifier('CODE/model/keras_model.h5', 'CODE/model/labels.txt')
#while True:
        #_, img = cap.read()
        #imgresize=cv2.resize(img,(454,340))
        #img =Image.open(fln)
        #img =Image.open(fln)
        #img.thumbnail((150,150))
imgbackground=cv2.imread('CODE/pic/cc.jpg')
        #copy relative path and call the fun by select image
img2=cv2.imread(fln)
predection = maskClassifier.getPrediction(img2)
print(predection)
'''
 if(predection=="2 GLASS"):
   print("recy")
 else:
   print("not found")
'''
 
imgresize=cv2.resize(img2,(454, 340))
imgbackground[148:148+340, 159:159 + 454]=imgresize

imgbackground2=cv2.imread('code/pic/arrow.png')
 #imgbackground=cvzone.overlayPNG(imgbackground,imgwaste[0],[909,107])

imgresize2=cv2.resize(imgbackground2,(454, 340))
imgbackground[148:148+340, 159:159 + 454]=imgresize2
 #imgbackground = cvzone.overlayPNG( imgbackground,imgwaste[0],(909,127))
 #cv2.imshow("bgimg", imgbackground2)
cv2.imshow("bgmi",imgbackground)
 #cv2.imshow("bgmi2",imgres)



        #cv2.imshow("CLASSIFIER ", img2)
cv2.waitKey(0)
