#!/usr/bin/python3

from PIL import Image
import numpy as np
import scipy.misc as sc
import scipy.spatial as ss
import sys

feature_images = ['sea1.png','sea2.png','sea3.png','lake.png','builtup.png',
                  'vegetation1.png', 'vegetation2.png', 'vegetation3.png',
                  'vegetation4.png']
sea_class = ['sea1.png','sea2.png','sea3.png']
lake_class = ['lake.png']
builtup_class = ['builtup.png']
vegetation_class = ['vegetation1.png','vegetation2.png',
                    'vegetation3.png','vegetation4.png']

def calc_mean_pixel(imgs):
    sum_pix = 0
    n_pix = 0
    for img in imgs:
        im = sc.imread(img)
        this_n_pix = np.size(im)//3
        im2 = np.reshape(im, [this_n_pix,3])
        n_pix = n_pix + this_n_pix
        #print(np.sum(im2,1))
        sum_pix = np.add(sum_pix,np.sum(im2,0))
    return (np.divide(sum_pix,n_pix))

mean_pixel = [calc_mean_pixel(sea_class), calc_mean_pixel(lake_class),
              calc_mean_pixel(vegetation_class), calc_mean_pixel(builtup_class)]

main = sc.imread('mumbai.png')

argmin_to_feature = [[0,0,0], # sea
                     [75,75,75], # lake
                     [128,128,128], # vegetation
                     [255,255,255]] # builtup

def map_to_feature(pix):
    dist = []
    if (sys.argv[1] == 'eu'):
        for i in range(4):
            dist.append(ss.distance.euclidean(pix,mean_pixel[i]))
    elif (sys.argv[1] == 'man'):
        for i in range(4):
            dist.append(ss.distance.cityblock(pix,mean_pixel[i]))
    return argmin_to_feature[np.argmin(dist)]

(x_max,y_max, z) = np.shape(main)
#print(np.size(main))
for i in range(x_max):
#    print(i)
    for j in range(y_max):
        main[i][j] = map_to_feature(main[i][j])

filename=''
if (sys.argv[1] == 'eu'):
    filename = 'segmented_eu.png'
elif (sys.argv[1] == 'man'):
    filename = 'segmented_man.png'
sc.imsave(filename,main)    
    


