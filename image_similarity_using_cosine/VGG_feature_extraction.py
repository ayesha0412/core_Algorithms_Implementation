# <!-- #Having a serach image based on an image kinda seraches your list of images(database) and which one ranks on top. 
# -> using VGG16 & Cosine similarity 
# -> trained on image net and it's CNN
# -> You can cut this archetecture and can use this as features.
# -To search for images you need to capture/ content of images as vectors typically feature vectors.
# -> You can use your feature descriptors like Gabor filter for edge detection and combine everything into a single vector or take pre trained and chop it off at one point.
# -> 512 lenghth by end the features your image contain
# -> Query image (generated features) is get matched with these values plotted on a graph
# -> How to compare vectors:
# 512 dimensions get mapped to 3D using PCA(Principal component Analysis)
# -->


import numpy as np
from numpy import linalg as LA