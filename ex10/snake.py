from queue import Queue


class Snake:
    color: str = "black"

    def __init__(self):
        self.body = Queue()
        for i in range(3):
            self.body.enqueue((10, 8+i))
        self.direction = "Up"

    def snake_coordinates(self):
        return self.body.get_content()

    def possible_moves(self):
        all_moves = ["Up", "Down", "Right", "Left"]
        if self.direction == "Up":
            all_moves.remove("Down")
        elif self.direction == "Down":
            all_moves.remove("Up")
        elif self.direction == "Right":
            all_moves.remove("Left")
        elif self.direction == "Left":
            all_moves.remove("Right")
        return all_moves

    def set_direction(self, direction: str):
        if direction in self.possible_moves():
            self.direction = direction

    def _next_location(self):
        current = self.body.get_tail() # tail - end of queue
        print(current)
        if self.direction == "Up":
            return current[0], current[1] + 1
        elif self.direction == "Down":
            return current[0], current[1] - 1
        elif self.direction == "Right":
            return current[0] + 1, current[1]
        elif self.direction == "Left":
            return current[0] - 1, current[1]

    def grow_by_one(self):
        self.body.enqueue(self._next_location())

    def move(self):
        self.grow_by_one()
        self.body.dequeue()

    def check_collision(self):
        return len(set(self.snake_coordinates())) != self.body.get_size()