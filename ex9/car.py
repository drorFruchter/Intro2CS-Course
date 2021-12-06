class Car:
    """
    Add class description here
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
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
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
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        #For this car type, keys are from 'udrl'
        #The keys for vertical cars are 'u' and 'd'.
        #The keys for horizontal cars are 'l' and 'r'.
        #You may choose appropriate strings.
        # implement your code and erase the "pass"
        #The dictionary returned should look something like this:
        #result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        #A car returning this dictionary supports the commands 'f','d','a'.
        pass

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        #For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        #be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        pass

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        pass

    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        pass
