# TODO: Implement generic serial comm device object
class Camera(object):
    
    def __init__(self, name, link, resolution):
        super(Camera, self).__init__()
        self.name = name
        self.link = link
        self.resolution = resolution


class Screen(object):
    
    def __init__(self, name):
        super(Screen, self).__init__()
        self.name = name


class Video(Screen):

    def __init__(self, name, link):
        super(Video, self).__init__(name)
        self.link = link


class FlatScreen(Screen):

    def __init__(self, name, color):
        super(FlatScreen, self).__init__(name)
        self.color = color
