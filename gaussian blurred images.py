import numpy as np
import plotly.express as px
from skimage import io
from skimage import filters

#read images
img = io.imread('images/saruman.jpg')
fig = px.imshow(img)


#adding a gaussian blur to image, kind of like in photoshop
sigmas = [10]

img_sequence = [filters.gaussian(img, sigma=sigma) for sigma in sigmas]
fig = px.imshow(np.array(img_sequence), facet_col=0, binary_string=True,
                labels={'facet_col':'sigma'})

for i, sigma in enumerate(sigmas):
    fig.layout.annotations[i]['text'] = 'sigma = %d' %sigma


#removing the x & y axis labels as they are unnecessary for this project
fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)


fig.show()