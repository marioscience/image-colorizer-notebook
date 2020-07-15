import glob
import numpy as np
from matplotlib import pyplot as plt
from keras.preprocessing.image import load_img

images_glob = glob.glob('/home/mario/Downloads/image-datasets/unlabeled2017_subsample/*.jpg')

images = np.array([np.array(load_img(img_path)) for img_path in images_glob])

len(images[0][0][0])

first_img = images[0]

print("started")

for i, elem_i in len(first_img):
    for j, elem_j in len(first_img):
        sum_colors = first_img[i][j][0] + first_img[i][j][1] + first_img[i][j][2]
        first_img[i][j][0] = sum_colors/3
        first_img[i][j][1] = sum_colors/3
        first_img[i][j][2] = sum_colors/3

plt.imshow(first_img[0][0][2])
plt.show()
