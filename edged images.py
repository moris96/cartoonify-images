import cv2
import plotly.express as px
from skimage import io

#read images
img = io.imread('images/saruman.jpg')
fig = px.imshow(img)


#edged image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)

fig = px.imshow(edges)


#removing the x & y axis labels as they are unnecessary for this project
fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)


fig.show()