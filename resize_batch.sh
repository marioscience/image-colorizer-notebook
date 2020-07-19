#!/bin/bash

WIDTH=300
HEIGHT=300
IMG_DIR="/home/mario/MIU/ML/final-project/image-colorizer-notebook/unlabeled2017_subsample/"

# use command below to copy a number of samples from original files to a folder to work in
# find . -type f -name *.jpg -print0 | xargs -0 shuf -e -n 600 -z | xargs -0 cp -t /home/mario/Downloads/image-datasets/unlabeled2017_subsample/

# use this command to convert all images in the target directory replacing them for 300x300 centered (remainders cropped) images
find ${IMG_DIR} -iname '*.jpg' -exec convert \{} -resize x600 -resize '600x<' -resize 50% -gravity center -crop 300x300+0+0 +repage \{} \;
