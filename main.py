
# import some related package and external plugins
import os
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from osgeo import  gdal

# Reading the original data to the project
def readdata(filename):
    data = np.loadtxt(filename)
    # a text of print
    print('data load finsh')
    return data

# Writing txt format to tiff format file, pass in the relevant parameters and output the appropriate image
def writetif(data,Xize,Yszie,inputname):
    fileformat = "GTiff"
    driver = gdal.GetDriverByName(fileformat)
    dst_ds = driver.Create(inputname, xsize=Xize, ysize=Yszie,
                           bands=1, eType=gdal.GDT_Byte)
    dst_ds.GetRasterBand(1).WriteArray(data)
    return data

# the main function of D8Algorithm, implementation of principle of operation of D8Algorithm
def D8Algorithm(data,Xsize,Yszie):
    # Store the coordinate of x,y in two-dimensional arrays
    vector = [[0] * Xsize for i in range(Yszie)]
    # Calculating the distance from eight points around the centre point to the centre point
    for i in range(len(data)):
        for j in range(len(data[0])):
            S = data[i][j] - data[i + 1][j] if i != Xsize-1 else -1
            SE = (data[i][j] - data[i + 1][j + 1]) / sqrt(2) if(i != (Xsize - 1) and j != (Ysize - 1)) else -1
            N = data[i][j] - data[i - 1][j] if (i != 0) else -1
            E = (data[i][j] - data[i][j + 1])if (j != (Ysize - 1)) else -1
            NE =(data[i][j] - data[i - 1][j + 1]) / sqrt(2) if (i != 0 and j != (Ysize - 1)) else -1
            NW = (data[i][j] - data[i - 1][j - 1]) / sqrt(2)if(i != 0 and j != 0) else -1
            W = (data[i][j] - data[i][j - 1]) if(j != 0) else -1
            SW = (data[i][j] - data[i + 1][j - 1]) / sqrt(2)if(i != (Xsize - 1) and j != 0) else -1
            # Storing the maximum value in an array
            LISTD8 = [S,SE,N,E,NE,NW,W,SW]
            MAX_LISTD8=max(LISTD8)
            INDEX=LISTD8.index(MAX_LISTD8)
            #  a print of test
            print(INDEX)
            # Assigning a speical value to the maximum value in each direction
            if MAX_LISTD8>0:
                #S位置
                if INDEX == 0:
                    vector[i][j] = 4
                elif INDEX ==1 :
                    vector[i][j] = 2
                elif INDEX == 2:
                    vector[i][j] = 64
                elif INDEX ==3 :
                    vector[i][j] = 1
                elif INDEX ==4 :
                    vector[i][j] = 128
                elif INDEX ==5 :
                    vector[i][j] = 32
                elif INDEX == 6:
                    vector[i][j] = 16
                elif INDEX ==7:
                    vector[i][j] = 8
            else:
                vector[i][j] = 0
    return np.array(vector)


if __name__ == '__main__':
    # Naming some files
    filename='snow.slope.txt'
    inputname='DEM.tif'
    resultname = 'D8_original_result.tif'
    data=readdata(filename)
    X=np.shape(data)
    Xszie=X[0]
    Ysize=X[1]
    # Passing in parameters to the function of D8
    vector=D8Algorithm(data,Xszie,Ysize)
    print(np.shape(vector))
    # Exporting the original unprocessed image
    writetif(data,Xszie,Ysize,inputname)
    writetif(vector,Xszie,Ysize,resultname)
    INTvector = vector.astype(np.int64)
    print(INTvector)
    # Statements for exporting original and decorated output images and text
    np.savetxt('D8Result.txt',INTvector, fmt='%d',header ='D8 slop output file')
    plt.title("Slope_map of Algorithm D8")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.imshow(vector,cmap='viridis')
    plt.savefig('D8_decorated_result.jpg', facecolor='grey', edgecolor='black')
    plt.colorbar()
    plt.show()
