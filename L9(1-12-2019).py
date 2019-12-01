#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:07:57 2019

@author: owner
"""

#EX1
"""
import statistics as st
print(st.mean([1, 2, 3, 4, 4]))
x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))
"""
#EX2
"""
import random
print( random.random() )
print ( random.randrange(10) )
print ( random.choice(['Ali', 'Khalid', 'Hussam']) )
print ( random.sample(range(1000), 10) )
print ( random.choice('orange Academy') )
items = [1,5,8,9,2,4]
random.shuffle(items)
print( items )
print ( random.randint(20,30) )
print ( random.randrange(1000, 2111, 5) )
print ( random.uniform(10000, 11000))
"""
#EX3:
"""
import math
print("pi= ",math.pi)
print ("cos(200)=" ,math.cos(200))
print ("sin(30)=" ,math.sin(30))
print ("tan(180)=" ,math.tan(180))
print(math.floor(10.8))
print(math.ceil(10.8))
"""
#EX4:
from PIL import Image,ImageDraw,ImageFilter
im=Image.open("cat.jpg")
img2=Image.open("dog.jpeg").resize(im.size)
"""
print(im.format,im.size,im.mode)
im.show()

im2 = im.transpose(Image.FLIP_LEFT_RIGHT) 
im2.show()
gray=im.convert('L')
gray.show()

cropped=im.crop((0,0,50,50))
cropped.show()
"""

"""
draw=ImageDraw.Draw(im)
draw.line((0,0)+im.size, fill = (225,225,225))
draw.line((0,im.size[1], im.size[0],0),fill=(225,225,225))
draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2+20),'Hala',fill=(225,225,0))
draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2-60),'Image',fill=(225,225,0))
im.show()
"""
"""
newImage2=im.filter(ImageFilter.SHARPEN)
newImage2.show()
newImage2=im.filter(ImageFilter.EDGE_ENHANCE)
newImage2.show()
newImage3=im.filter(ImageFilter.FIND_EDGES)
newImage3.show()
newImage4=im.filter(ImageFilter.SMOOTH)
newImage4.show()
"""
"""
Image.blend(im,img2,0.5).save('newimg.jpg'.format(0.5))
im1=Image.open('newimg.jpg')
im1.show()
"""
"""
original=Image.open("cat.jpg")
blurred=original.filter(ImageFilter.BLUR)
blurred.show()
blurred.save("blurred.jpg")
"""
"""
size=(128,128)
saved="img4.jpg"
try:im
except:print("Unable to load image")
im.thumbnail(size)
im.save(saved)
im.show()
"""
"""
im1_flip=img2.transpose(Image.ROTATE_90)
im1_flip.show()
"""
mask=Image.open('mask.jpg')
mask=mask.resize(im.size)
Image.composite(im,img2,mask).save('maskimage.jpg')
imagMask=Image.open('maskimage.jpg')
imagMask.show()
