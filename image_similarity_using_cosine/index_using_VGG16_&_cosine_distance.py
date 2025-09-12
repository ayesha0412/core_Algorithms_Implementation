import os
import h5py #it's like our database to store features
import numpy as np
from VGG_feature_extraction import VGGNet


images_path="./images/"
img_list=[os.path.join(images_path,f) for f in os.listdir(images_path)]

print("Start feature extraction...")
model=VGGNet()
path="/images"
feats=[]
names=[]
for im in os.listdir(path):
    print("Extracting feature from image %s" %im)
    x=model.extract_feat(path+im)

    feats.append(x)
    names.appnend(im)

feats=np.array(feats)


output="CNNFeatures.h5"
print("Writing feature to CNNFeatures.h5")
h5f=h5py.File(output,'w')
h5f.create_dataset('dataset_1',data=feats)
h5f.create_dataset('dataset_2',data=np.bytes(names))
h5f.close()
print("Finished successfully!")
