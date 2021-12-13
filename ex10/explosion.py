class Explosion:
    def __init__(self, radius: int, location: (int, int)):
        self.__radius: int = radius
        self.__location: (int, int) = location
        self.__exploded_cells: list[(int, int)] = []

    def start_explosion(self, time_from_explosion: int) -> list:
        x = self.__location[0]
        y = self.__location[1]
        for row in range(x - time_from_explosion, x + time_from_explosion + 1):
            for col in range(y - time_from_explosion, y + time_from_explosion + 1):
                if abs(x - row) + abs(y - col) == time_from_explosion:
                    self.__exploded_cells.append((row, col))
        return self.__exploded_cells



