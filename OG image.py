import plotly.express as px
from skimage import io

#read the image
img = io.imread('images/saruman.jpg')
fig = px.imshow(img)

#removing the x & y axis labels as they are unnecessary for this project
fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)


fig.show()