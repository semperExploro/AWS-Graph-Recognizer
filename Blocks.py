

class Blocks:

    def __init__(self, response):
        """
        response: a dictionary of the response from AWS Textract
        """
        self.text = response['Text']
        self.Geometry = response['Geometry']['BoundingBox']
        self.Polygon = response['Geometry']['Polygon']
        self.Centroid= self._centroid()
        self.LocationImage = None
        self.Height = None
        self.Width = None

    def setHeight(self,img):
        # set height of bounding box of text
        self.Height = int(self.Geometry['Height'] * len(img))
    
    def setWidth(self,img):
        # set width of bounding box of text
        self.Width = int(self.Geometry['Width'] * len(img[0]))

    def _centroid(self):
        # find centroid of bounding box of text
        x = 0
        y = 0
        for point in self.Polygon:
            x += point['X']
            y += point['Y']
        x /= len(self.Polygon)
        y /= len(self.Polygon)
        return (x, y)

    def locationInImage(self,img):
        # find location of centroid in image
        x = int(self.Centroid[0] * len(img[0]))
        y = int((self.Centroid[1]) * len(img))
        self.LocationImage = (x,y)
    