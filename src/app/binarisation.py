import cv2 as cv
import numpy as np

"""
adaptive thresholding using integral image, Gerhard Roth
check this link: https://www.researchgate.net/publication/220494200_Adaptive_Thresholding_using_the_Integral_Image
"""
def adaptive_threshold_integral_img(image,  sub_thresh = 0.15):
    # entre 0 et 1 
    #image = cv.imread(filename)
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    #Calculate integral image
    integralimage = cv.integral(gray_image, cv.CV_32F)
    
    width = gray_image.shape[1]
    height = gray_image.shape[0]
    win_length = int(width / 8)
    image_thresh = np.zeros((height, width), dtype = np.uint8)
    #perform threshholding
    for i in range(height):
        for j in range(width):
            x1 = int(i - win_length/2)
            x2 = int(i + win_length/2)
            y1 = int(j - win_length/2)
            y2 = int(j + win_length/2)
            
            #check the border
            if(x1 <= 0):
                x1 = 1
            if(y1 <= 0):
                y1 = 1
            if(x2 > height):
                x2 = height -1
            if(y2 > width):
                y2 = width -1
            count = (x2- x1) * (y2 - y1)

            sum = integralimage[x2, y2] - integralimage[x2, y1-1] -integralimage[x1-1, y2] + integralimage[x1-1, y1-1]
            if (int)(gray_image[i, j] * count) <= (int) (sum * (1.0 - sub_thresh)):
                image_thresh[i, j] = 0
            else:
                image_thresh[i, j] = 255
    print("sortie dengin")
    return image_thresh

#simple opencv otsu's binarization
def adaptive_threshold_otsu(img):
    if len(img.shape) !=2:
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(img,(3,3),0)
    out_img= cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    return out_img


"""
print("color val ",  cv.IMREAD_COLOR)

img = cv.imread("data/image4.jpg",cv.IMREAD_COLOR)

img = adaptive_threshold_integral_img(img)    
cv.imshow("the method2", img)
cv.waitKey(0)
cv.destroyAllWindows()

"""