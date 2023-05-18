## Protoype Line Graph Point Extractor 

### Description
Prototype for extracting points from a graph - specifically for line graphs. 

### File List 
* `README.md` - this file
* `lineGraphPtRecognition.py` - script to extract text from AWS textract, specifically axis labels and other labels. This file is incomplete (see next steps)
* `Blocks` - represents a class representation of labels and text within a graph element
* `imageProcessing.ipynb` - script to extract points from a line graph. 
* `sampleImages` - folder containing sample images to test the script on.

### Requirements
* Python 3+
* Use `pip install` for the following
   * boto3
   * openCV-python
   * numpy
   * matplotlib
   * extcolors

### Usage
* `python3 lineGraphPtRecognition.py`
* `jupyter notebook imageProcessing.ipynb`

### Next Steps
* Complete `lineGraphPtRecognition.py` to extract axis text. The problem arises when not all the text's centroid are aligned for a given axis. Eg the y axis labels are not aligned uniformly. 

    * Extension - scale the points of the CV (Computer Vision) extracted points to a fit the scale of the graph.

* Complete `lineGraphPtRecognition.py` to block out text in the original graph image to prevent confusion when processing the image when using computer vision. Should choose the same color as background when whitting out text. 

