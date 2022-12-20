import os
import re


def checkDirectory(directoryPath):
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)


def extractResult(outputDirectory, fileName, regexPattern):

    file = open("{}/{}".format(outputDirectory, fileName))
    text = file.read()

    matchObjList = re.findall(regexPattern, text, re.M|re.I)

    return matchObjList
