import cv2
import numpy as np

path='data/image3.jpg'
voisinage=3

#just in case we find a solution to use it on an image
kernel3D=np.array([
        [[0,0,0],[0,-1,0],[0,0,0]],
        [[0,-1,0],[-1,6,-1],[0,-1,0]],
        [[0,0,0],[0,-1,0],[0,0,0]]
        ])

#its results look better
def laplacian_filter(img):
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    result=cv2.Laplacian(img_gray,cv2.CV_16S,ksize=3)
    result=cv2.convertScaleAbs(result)
    return result

#the function that we did in tp
def laplacian_other(img):
    kernel=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    result=cv2.filter2D(img,-1,kernel)
    return result

    
def gaussian_filter(img):
    result=cv2.GaussianBlur(img,(3,3),0)
    return result

#3D mean filter, cant be used with laplacian filter
def mean_filter(img):
    h,w,c=img.shape
    img_moy= np.zeros(img.shape,np.uint8)

    for y in range(h):
        for x in range(w):
            for z in range(c):
                if x<voisinage/2 or x>w-voisinage/2 or y<voisinage/2 \
                    or y>h-voisinage/2:
                    img_moy[y,x,z]=img[y,x,z]
                
                else:
                    imgV= img[int(y-voisinage/2):int(y+voisinage/2)+1,\
                        int(x-voisinage/2):int(x+voisinage/2)+1,z]
                    
                    img_moy[y,x,z]=np.mean(imgV)
    return img_moy


#3D median filter, cant be used with laplacian filter
def median_filter(img):
    h,w,c=img.shape
    img_med= np.zeros(img.shape,np.uint8)

    for y in range(h):
        for x in range(w):
            for z in range(c):
                if x<voisinage/2 or x>w-voisinage/2 or y<voisinage/2 \
                    or y>h-voisinage/2:
                    img_med[y,x,z]=img[y,x,z]
                
                else:
                    imgV= img[int(y-voisinage/2):int(y+voisinage/2)+1,\
                        int(x-voisinage/2):int(x+voisinage/2)+1,z]
                    
                    img_med[y,x,z]=np.median(imgV)
    return img_med


#used with 2D images (images that used laplace)
def median_2D(img):
    h,w=img.shape
    img_med= np.zeros(img.shape,np.uint8)

    for y in range(h):
        for x in range(w):
                if x<voisinage/2 or x>w-voisinage/2 or y<voisinage/2 \
                    or y>h-voisinage/2:
                    img_med[y,x]=img[y,x]
                
                else:
                    imgV= img[int(y-voisinage/2):int(y+voisinage/2)+1,\
                        int(x-voisinage/2):int(x+voisinage/2)+1]
                    
                    img_med[y,x]=np.median(imgV)
    return img_med


#used with 2D images (images that used laplace)
def mean_2D(img):
    h,w=img.shape
    img_mean= np.zeros(img.shape,np.uint8)

    for y in range(h):
        for x in range(w):
                if x<voisinage/2 or x>w-voisinage/2 or y<voisinage/2 \
                    or y>h-voisinage/2:
                    img_mean[y,x]=img[y,x]
                
                else:
                    imgV= img[int(y-voisinage/2):int(y+voisinage/2)+1,\
                        int(x-voisinage/2):int(x+voisinage/2)+1]
                    
                    img_mean[y,x]=np.mean(imgV)
    return img_mean



if __name__ == '__main__':
    img=cv2.imread(path,cv2.IMREAD_COLOR)
    gauss=gaussian_filter(img)
    filtered1=laplacian_filter(gauss)
    #filtered2=laplacian_other(gauss)
    filtered3=mean_2D(filtered1)

    cv2.imshow('original image',img)
    #cv2.imshow("gaussian img",gauss)
    #cv2.imshow("both img",filtered1)
    #cv2.imshow("other img",filtered2)
    cv2.imshow("mean img",filtered3)
    
    cv2.waitKey()
    cv2.destroyAllWindows()