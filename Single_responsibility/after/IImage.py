# interface of image

class IImage:

    def __init__(self, width, height, path):

        self.width = width
        self.height = height
        self.path = path
        # TODO uploading part....

    def get_image(self):
        raise NotImplementedError