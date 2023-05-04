"""
Module for class Node.
"""
from random import uniform
from random import randint
from uuid import uuid1
from math import sqrt
from clock import Clock

class Node(Clock):
    """
    Class for representation of a node inside a network that has an internal clock.
    """
    def __init__(self,
                 position: tuple[int, int],
                 transmission_range: float,
                 natural_skew: float,
                 initial_offset: int) -> None:
        super().__init__(1 - uniform(-natural_skew, natural_skew),
                         randint(-initial_offset, initial_offset))
        self.uid = uuid1()
        self.position = position
        self.transmission_range = transmission_range
        self.active = True

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Node \033[31m{self.uid}\033[39m at coordinates {self.position}.\n"

    def move_to(self, new_position: tuple[int, int]) -> None:
        """
        Move the node to another position.
        """
        self.position = new_position

    def turn_off(self) -> None:
        """
        Disable the node.
        """
        if self.active is True:
            self.active = False
        else:
            print(f"Node \033[31m{self.uid}\033[39m is already off.\n")

    def turn_on(self) -> None:
        """
        Activate the node.
        """
        if self.active is False:
            self.active = True
        else:
            print(f"Node \033[31m{self.uid}\033[39m is already on.\n")

    def in_range(self, receiver_position: tuple[float, float], receiver_uid: str) -> bool:
        """
        Check if receiver node is in trasmission range of the sender node.
        """
        # Check if node is not itself
        if self.uid != receiver_uid:
            x_position, y_position = receiver_position
            distance = sqrt((self.position[0] - x_position)**2 + (self.position[1]-y_position)**2)
            # Check distance is in range
            if distance <= self.transmission_range:
                return True

        return False

if __name__ == "__main__":
    pass
    # Test code for class Node
    #exampleNode = Node((0,0), 1)
    #exampleNode.turn_on()
    #exampleNode2 = Node((1,1), 1)
    #print(exampleNode2)
