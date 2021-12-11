#################################################################
# FILE : car.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex9 2021
# DESCRIPTION: Car class
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
class Car:
    """
    A class that presents a car
    """

    def __init__(self, name: str, length: int,
                 location: (int,int), orientation: int):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name: str = name
        self.length: int = length
        self.location: (int, int) = location
        self.orientation: int = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        row, col = self.location[0], self.location[1]
        co_lst = []
        for i in range(self.length):
            if self.orientation == 0:
                co_lst.append((row+i, col))
            else:
                co_lst.append((row, col+i))
        return co_lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible
                 movements permitted by this car.
        """
        if self.orientation == 0:
            result = {'u': "cause the car to go UP",
                      'd': "cause the car to go DOWN"}
        elif self.orientation == 1:
            result = {'r': "cause the car to go RIGHT",
                      'l': "cause the car to go LEFT"}
        else:
            result = {}

        return result

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty
                 in order for this move to be legal.
        """
        required_lst = []
        if movekey == "u":
            required_lst.append((self.location[0]-1, self.location[1]))
        elif movekey == "d":
            required_lst.append((self.location[0] + self.length,
                                 self.location[1]))
        elif movekey == "r":
            required_lst.append((self.location[0],
                                 self.location[1]+self.length))
        elif movekey == "l":
            required_lst.append((self.location[0], self.location[1]-1))

        return required_lst

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey in self.possible_moves():
            if movekey == "u":
                self.location = (self.location[0] - 1, self.location[1])
            elif movekey == "d":
                self.location = (self.location[0] + 1, self.location[1])
            elif movekey == "r":
                self.location = (self.location[0], self.location[1] + 1)
            elif movekey == "l":
                self.location = (self.location[0], self.location[1] - 1)
            return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name
