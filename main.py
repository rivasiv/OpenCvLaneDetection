from LaneDetection import LaneDetection
import os
import glob

def main():

    # Get all files in a folder
    dataSetFolder = "caltech-lanes/cordova1"
    allImages = glob.glob(os.path.join(dataSetFolder, "*.png"))

    laneDetection = LaneDetection()
    laneDetection.process("original.bmp")
    laneDetection.showOrgImage()

    #processImage([allImages[0]])
    #processImage(allImages)

if __name__ == "__main__":
    main()