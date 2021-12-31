import cv2
import numpy as np

path='data/image1.png'

#just in case we find a solution to use laplacian in 3D, this is its kernel
kernel3D=np.array([
        [[0,0,0],[0,-1,0],[0,0,0]],
        [[0,-1,0],[-1,6,-1],[0,-1,0]],
        [[0,0,0],[0,-1,0],[0,0,0]]
        ])

#its results look better
def laplacian_filter(img):
    if len(img.shape)!=2 :
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else :
        img_gray=img

    result=cv2.Laplacian(img_gray,cv2.CV_16S,ksize=3)
    result=cv2.convertScaleAbs(result)
    return result

#improves clarity
def improve_image(img):

    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    result=cv2.filter2D(img,-1,kernel)
    return result


def laplacian_8_connex(img):
    if len(img.shape)!=2 :
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel=np.array([[1,1,1],[1,-8,1],[1,1,1]])
    result=cv2.filter2D(img,-1,kernel)
    return result

def laplacian_robinson(img):
    if len(img.shape)!=2 :
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    kernel=np.array([[1,-2,1],[-2,4,-2],[1,-2,1]])
    result=cv2.filter2D(img,-1,kernel)
    return result

    
def gaussian_filter(img):
    result=cv2.GaussianBlur(img,(3,3),0)
    return result


#3D mean filter, cant be used with laplacian filter
#user enters voisinage
def mean_filter(img,voisinage):
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
#user enters voisinage
def median_filter(img,voisinage):
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
def median_2D(img,voisinage):
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
def mean_2D(img,voisinage):
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


#works for both 3D and 2D
# User enters sizeDelate
def delate_func(img,sizeDelate):
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(sizeDelate*2+1,sizeDelate*2+1))
    result=cv2.dilate(img,kernel,iterations=1)
    return result

# User enters sizeErode
def erode_func(img,sizeErode):
    kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(sizeErode*2+1,sizeErode*2+1))
    result=cv2.erode(img,kernel,iterations=1)
    return result

# User enters sizeOuverture
def ouverture_func(img,sizeOuverture):
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(sizeOuverture*2+1,sizeOuverture*2+1))
    result=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    return result

# User enters sizeFermeture
def fermeture_func(img,sizeFermeture):
    kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(sizeFermeture*2+1,sizeFermeture*2+1))
    result=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
    return result


#re-scales the image
def resize_image(img,scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    return resized


if __name__ == '__main__':
    img=cv2.imread(path,cv2.IMREAD_COLOR)
    gauss=gaussian_filter(img)
    #filtered1=laplacian_filter(img)
    #improved=improve_image(img)
    #result1=laplacian_filter(gauss)
    #filtered2=laplacian_other(gauss)
    filtered3=mean_filter(img,3)
    #mean=fermeture_func(img)
    #filtered4=ouverture_func(gauss)
    #filtered5=fermeture_func(gauss)

    filtered3=resize_image(filtered3,80)
    #cv2.imshow('original image',img)
    cv2.imshow("laplacian",filtered3)
    #cv2.imshow("both img",improved)
    #cv2.imshow("other img",filtered2)
    #cv2.imshow("ouverture img",filtered4)
    #cv2.imshow("fermeture img",filtered5)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
