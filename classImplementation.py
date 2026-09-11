class Instruments:
    def __init__(self, type: str, material: str, name: str, is_tune: bool = False):
        self.type = type
        self.material = material
        self.name = name  
        self.__is_tune = is_tune      # Private attribute

