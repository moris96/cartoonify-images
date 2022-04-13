import cv2
import plotly.express as px

#read image
img = cv2.imread('images/saruman.jpg')
fig = px.imshow(img)


#grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
fig = px.imshow(gray, color_continuous_scale='gray')


#removing the x & y axis labels as they are unnecessary for this project
fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)


fig.show()