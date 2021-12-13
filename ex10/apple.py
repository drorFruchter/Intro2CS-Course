class Apple:

    def __init__(self, location: (int, int), score: int) -> None:
        self.__location: (int, int) = location
        self.__score: int = score

    def get_location(self):
        return self.__location

    def get_score(self):
        return self.__score
