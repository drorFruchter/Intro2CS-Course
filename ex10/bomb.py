class Bomb:

    def __init__(self, location: (int, int), radius: int, timer: int) -> None:
        self.__location: (int, int) = location
        self.__radius: int = radius
        self.__timer: int = timer
        self.__explosion

    def get_location(self):
        return self.__location

