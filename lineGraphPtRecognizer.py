
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
import Blocks
import boto3


# Document
documentName = "sampleImages"+"/sampleOne.JPG"


# AWS 

# Read document content
with open(documentName, 'rb') as document:
    imageBytes = bytearray(document.read())

# Amazon Textract client
textract = boto3.client('textract')

# Call Amazon Textract
response = textract.detect_document_text(Document={'Bytes': imageBytes})


listOfText = []

# Get rid of texts
noTextImage = cv2.imread(documentName)

image = plt.imread(documentName)
#Get the Related Texts and initialize coordinates
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        newBlock = Blocks.Blocks(item)
        newBlock.locationInImage(image)
        newBlock.setHeight(noTextImage)
        newBlock.setWidth(noTextImage)
        listOfText.append(newBlock)


# identify axis
axisDistY = {}
axisDistX = {}

# go through each text
for item in listOfText:
    # Plot image
    plt.text(item.LocationImage[0], item.LocationImage[1], item.text, fontsize=12, color='red')
    print(item.LocationImage)

    # White out Text for image
    for row in range(item.LocationImage[1], item.LocationImage[1] + item.Height, 1):
        for col in range(item.LocationImage[0], item.LocationImage[0] + item.Width, 1):
            noTextImage[row][col] = [0, 0, 0]

    # Find Axis Numbers
    x = round(item.Centroid[0], 2)
    y = round(item.Centroid[1], 2)

    # using voting scheme to determine axis
    if x not in axisDistX:
        axisDistX[x] = 1
    else:
        axisDistX[x] += 1
    if y not in axisDistY:
        axisDistY[y] = 1
    else:
        axisDistY[y] += 1

# show image with location of text
plt.imshow(image)
plt.show()

# save image for no text
cv2.imwrite("noTextImage.jpg", noTextImage)


# ATTEMPTS TO FIND AXIS NUMBERS - Cannot be Done Because of the Positioning of the Numbers Could Be Anywhere

# xMax = max(axisDistX, key=axisDistX.get)
# yMax = max(axisDistY, key=axisDistY.get)

# xAxisValues = []
# for item in listOfText:
#     if round(item.Centroid[0],2) == xMax:
#         xAxisValues.append((item.text, item.Centroid[1]))

# yAxisValues = []
# for item in listOfText:
#     if round(item.Centroid[1],2) == yMax:
#         yAxisValues.append((item.text), item.Centroid[0])

# print(xAxisValues)
# print(yAxisValues)

# for item in xAxisValues:
#     plt.text(item[1], item[0], item[0], fontsize=12, color='red')