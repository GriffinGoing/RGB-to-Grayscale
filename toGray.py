import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


print("Loading image...")
img = cv2.imread('convertThis.jpg')

'''
For each pixel in the RGB image, the correlating pixel in 
the grayscale image will be the result of the following:
grayscale pixel = (.3 * red value) + (.59 * green value) + (.11 * blue value)

'''
print("Converting image...")
i = 0
for group in img:
    k = 0
    for pixel in group:
        #print(pixel)
        new = (.3 * pixel[0]) + (.59 * pixel[1]) + (.11 * pixel[2])
        img[i][k] = new
        k = k + 1
    i = i + 1
    

'''
Save the new grayscale image
'''
print("Saving img...")
cv2.imwrite('gray.jpg', img)

'''
Create a histogram of the pixel values. ravel() function
simply flattens the pixel array.
'''
print("Creating plots...")
fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)
axs.hist(img.ravel(), bins=255)

'''
Save the histogram
'''
print("Saving plot...")
plt.savefig('hist.jpg')

print("Done...")
