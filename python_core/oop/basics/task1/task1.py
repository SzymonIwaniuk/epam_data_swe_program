class Field:
    __value = None

    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def set_value(self, x):
        self.__value = x
