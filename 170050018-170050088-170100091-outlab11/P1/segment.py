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

dist=[]
if (sys.argv[1] == 'eu'):
    for feature in mean_pixel:
        diff = main - feature
        sq = np.multiply(diff,diff)
        eu_sum = np.sum(sq,2)
        dist.append(np.sqrt(eu_sum))
elif (sys.argv[1] == 'man'):
    for feature in mean_pixel:
        diff = main - feature
        dist.append(np.sum(np.abs(diff),2))

fin = main
#print(len(dist[0]))
        
def map_to_feature(i,j):
    #print(i,j)
    min_ind = np.argmin([dist[0][i][j],
                         dist[1][i][j],
                         dist[2][i][j],
                         dist[3][i][j]])
    #print(min_ind)
    return argmin_to_feature[min_ind]

(x_max,y_max, z) = np.shape(main)
for i in range(x_max):
#   print(i)
     for j in range(y_max):
         main[i][j] = map_to_feature(i,j)

filename=''
if (sys.argv[1] == 'eu'):
    filename = 'segmented_eu.png'
elif (sys.argv[1] == 'man'):
    filename = 'segmented_man.png'
sc.imsave(filename,main)    
    


