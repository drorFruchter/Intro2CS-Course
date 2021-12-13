from node import Node


class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def get_content(self):
        if not self.__head:
            return []
        pointer = self.__head
        lst = []
        while pointer != self.__tail:
            lst.append(pointer.get_data())
            pointer = pointer.next
        lst.append(pointer.get_data())
        return lst

    def get_head(self):
        return self.__head.get_data()

    def get_tail(self):
        return self.__tail.get_data()

    def get_size(self):
        return self.__size

    def is_empty(self):
        if self.__size > 0:
            return False
        else:
            return True

    def enqueue(self, item):
        if self.__tail == None:
            self.__head = Node(item)
            self.__tail = self.__head
        else:
            # adding new item to the end of the list
            self.__tail.next = Node(item)
            self.__tail = self.__tail.next
        self.__size += 1

    def dequeue(self):
        result = self.__head.get_data()
        self.__head = self.__head.next
        if self.__head == None:
            self.__tail = None
        self.__size -= 1
        return result
