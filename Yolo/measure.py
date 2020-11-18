#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import yolo
import webCam as wc
from keras.models import load_model
from math import ceil


# In[7]:

def getDist(im1, im2, m, model):
    a = getImgDim(im1, model)[0]
    b = getImgDim(im2, model)[0]

    dist = m/(1-(a/b))
    return ceil(dist)

def getImgDim(inImg, model):
    # inImg = '../pics/mob1.jpg'
    # model = load_model('yolo.h5')

    out_scores, out_boxes, out_classes = yolo.getBoxes(inImg, model)

    top = out_boxes[0][0]
    left = out_boxes[0][1]
    bottom = out_boxes[0][2]
    right = out_boxes[0][3]

    height = bottom-top
    width = right-left
    # area = height*width

    return height, width


def getRealDim(fl, dist, height, width):
    # realHeight = (dist*10000)/(fl * height)

    realHeight = (height*dist)/fl

    realWidth = (width*dist)/fl

    return realHeight, realWidth

## Test script
# im1 = '../pics/img1.JPG'
# im2 = '../pics/img2.JPG'
# model = load_model('yolo.h5')
# m = 5
#
# dist = getDist(im1, im2, m, model)
# height1, area1 = getImgDim(im1, model)
# height2, area2 = getImgDim(im2, model)
# fl = 25
#test
# rh1 = getRealDim(fl, dist, height1, area1)[0]
# rh2 = getRealDim(fl, dist, height2, area2)[0]
# avgH = (rh1+rh2)/2
# avgH = avgH + (0.2*avgH)
#
# rw1 = getRealDim(fl, dist, height1, area1)[1]
# rw2 = getRealDim(fl, dist, height2, area2)[1]
# avgW = (rw1+rw2)/2
# avgW = avgW + (0.2*avgW)
#
# print(avgH)
# print(avgW)

def main(im1, im2, m, fl, model):
    im1 = '../pics/'+im1
    im2 = '../pics/'+im2
    # model = load_model('yolo.h5')
    # m = 5

    dist = getDist(im1, im2, m, model)
    height1, width1 = getImgDim(im1, model)
    height2, width2 = getImgDim(im2, model)
    # fl = 25

    rh1 = getRealDim(fl, dist, height1, width1)[0]
    rh2 = getRealDim(fl, dist, height2, width2)[0]
    avgH = (rh1+rh2)/2
    # avgH = avgH + (0.2*avgH)

    rw1 = getRealDim(fl, dist, height1, width1)[1]
    rw2 = getRealDim(fl, dist, height2, width2)[1]
    avgW = (rw1+rw2)/2
    # avgW = avgW + (0.2*avgW)

    print(avgH/100)
    print(avgW/100)
    print(dist)

## Test Script
model = load_model('yolo.h5')

while(True):
    im1 = input('Enter the name of the 1st Image: \n')
    im2 = input('Enter the name of the 2nd Image: \n')

    main(im1=im1, im2=im2, m=5, fl=25, model=model)
    # print('Distance to the object',getDist(im1='../pics/'+im1, im2=im2, m=5, model=model))
