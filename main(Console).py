import numpy as np
import cv2
from multiprocessing.pool import ThreadPool

#Made by Ed Lynch licenced under the Apache 2.0 licence

pool = ThreadPool(processes=4)


#Percent Holder
percentage = [0,0,0,0]

 #Holds output of imageToJS function
imageCodeHolder = ["","","",""]

def imageToJS(start, end, x, addTo, image = []):
    imageCode = ""
    #Go through each pixel of the image
    for i in range(start,end):
        #Calculate pct complete
        pct = (float(i)/ float(end))*100
        #Update text if decimal of 5 (minimise calculations)
        if( round(pct) % 5 == 0 and pct !=0):
            #Assign the new percentage to the relavent index in the percentage array
            percentage[addTo] = int(round(pct))
            #Get the mean of all the percentages
            pct = sum(percentage)/4
            print( str(round(pct))+ "%")
        for j in range(0,x):
            #add code for this pixel
           imageCode += 'ctx.beginPath();\n'
           imageCode += 'ctx.fillRect('+str(j)+','+str(i)+',1,1);\n'
           imageCode += "ctx.fillStyle = 'rgb({},{},{})';\n".format(image[i][j][2], image[i][j][1], image[i][j][0])
           imageCode += 'ctx.stroke();\n'
           imageCode += 'ctx.closePath();\n'
    #Add to holder
    return imageCode


#Will make the image
def imageToSite(inputPath, outputPath):
    #Reset percentage
    percentage = [0,0,0,0]
    #Get the image and the size of it
    imagePath = inputPath
    image=cv2.imread(imagePath)
    y=image.shape[0] #length in first dimension
    x=image.shape[1] #length in second dimension
    #Define the canvas with the size of the image
    canvas = '<canvas id="myCanvas" width="{}" height="{}"></canvas>'.format(x, y)
    #Setup the canvas
    imageCode = "var c = document.getElementById('myCanvas');var ctx = c.getContext('2d');\n"

    #Run code to transform image to JS code in 4 threads to speed it up a notch
    t1 = pool.apply_async(imageToJS, (0, y/4, x, 0, image))
    t2 = pool.apply_async(imageToJS, (y/4, y/2, x, 1, image))
    t3 = pool.apply_async(imageToJS, (y/2, (y/2+y/4), x, 2, image))
    t4 = pool.apply_async(imageToJS, ((y/2+y/4), y, x, 3, image))

    #Add image code from holder to imageCode variable
    imageCode += (t1.get()+t2.get()+t3.get()+t4.get())

    #html code
    html = '<!DOCTYPE html>\n<html>\n<head>\n<title>Image to Canvas</title>\n</head>\n<body>\n{}\n</body>\n<script src="script.js"></script>\n</html>'.format(canvas)

    #Write to the html file
    f = open('index.html','w')
    f.write(html)
    f.close()

    #Write to the js file
    f = open('script.js','w')
    f.write(imageCode)
    f.close()

    print("Done")



#Holder for input and output paths
imageToSite("cat.jpg", "")
