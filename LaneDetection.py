import cv2
import numpy as np


class LaneDetection:
    def __init__(self):
        self.cannyThreshold1 = 50
        self.cannyThreshold2 = 50
        self.img = np.zeros((100, 100, 3), np.uint8)
        self.windowNameOrg = "Original"

    def runFileList(self, filelist):
        for element in filelist:
            self.process(element)

    def process(self, filename):
        self.img = cv2.imread(filename, cv2.IMREAD_COLOR)

    def showOrgImage(self, holdtime=0):
        cv2.imshow(self.windowNameOrg, self.img)
        cv2.waitKey(holdtime)
