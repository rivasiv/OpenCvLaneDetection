import cv2
import os
import glob
import numpy as np

def processImage(allImages):

    windowName = "VideoStream"
    cv2.namedWindow(windowName, flags=cv2.WINDOW_AUTOSIZE)

    houghVote = 200

    for fileName in allImages:
        img = cv2.imread(fileName, cv2.IMREAD_COLOR)
        orgimg = img.copy()
        edges = cv2.Canny(img, 50, 350, apertureSize=3)
        [_, contoursInv] = cv2.threshold(edges, 128, 255, cv2.THRESH_BINARY_INV)

        if houghVote < 1:
            houghVote = 200
        else:
            houghVote = houghVote + 25

        lines = cv2.HoughLines(contoursInv, 1, np.pi/180.0, houghVote)
        print(len(lines))


        cv2.imshow(windowName, contoursInv)
        cv2.waitKey(10)

    cv2.waitKey(0)

def main():

    # Get all files in a folder
    dataSetFolder = "caltech-lanes/cordova1"
    allImages = glob.glob(os.path.join(dataSetFolder, "*.png"))

    processImage(["original.bmp"])
    #processImage([allImages[0]])
    #processImage(allImages)

if __name__ == "__main__":
    main()