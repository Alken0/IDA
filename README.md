# Image-Datetime-Adder

This script allows to add datetimes to images based on their names.
The input-images should be either "png" or "jpg" images!

## How does it work?

1. Scan folder "data/originals" for all images
2. create copies of datetime-images and move them into "data/success"
    - jpg allows saving datetimes in files (png doesn't)
    - converts png automatically
3. move all non-fitting files into "data/failure"

## How to use it?

1. create the folder "data/originals" and move your images in this folder
    - all other folders are created automatically
2. ```pip install -r requirements.txt```
3. run all ```tests``` (just in case)
4. run ```main.py```
5. have a look at "data/success" and "data/failure"
