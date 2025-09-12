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
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input


#understanding the model
# model=VGG16(weights="imagenet",
#             input_shape=(224,224,3),
#             pooling='max',
#             include_top=False)
# model.summary()

class VGGNet:
    def __init__(self):
        self.input_shape=(224,224,3),
        self.weights="imagenet",
        self.pooling='max',
        self.model=VGG16(weights=self.weights,
                         input_shape=(self.input_shape[0],self.input_shape[1],self.input_shape[2]),
                         pooling=self.pooling,
                         include_top=False
                         )
        
'''usee VGG16 to extract features from an image'''
def extract_features(self,img_path):
    img=image.load_img(img_path,target_size=(self.input_shape[0],self.input_shape[1]))
    img=image.img_to_array(img)
    img=np.expand_dims(img,axis=0)
    img=preprocess_input(img)
    feat=self.model.predict(img)
    norm_feat=feat[0]/LA.norm(feat[0])
    return norm_feat