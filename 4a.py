import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.png',0)
cv2.imshow('original',img)
hist,bins = np.histogram(img.flatten(),256,[0,256])
hh = hist
hh_normalized = hh * hist.max()/ hh.max()
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()
hh_m = np.ma.masked_equal(hh,0)
hh_m = (hh_m - hh_m.min())*255/(hh_m.max()-hh_m.min())
hh = np.ma.filled(hh_m,0).astype('uint8')
img2 = hh[img]
cv2.imwrite('result.png' ,img2)
img22 = cv2.imread('result.png',0)
cv2.imshow('result',img22)
cv2.waitKey(0)
cv2.distroyAllWindows()


