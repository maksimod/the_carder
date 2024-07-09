class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y

    def __check_value(cls):



pt = Point(1,2)
print(pt.get_coord())