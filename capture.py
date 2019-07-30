import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from numpy import uint8, float32, float64, log, pi, sin, cos, abs, sqrt
from scipy.ndimage.filters import convolve

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break
    
    ret, frame = cap.read()
    if not ret: continue
    cv2.imshow('title', frame)  # show in the win
    
plt.close()
cap.release()
cv2.destroyAllWindows()

