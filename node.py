from math import sqrt
from uuid import uuid1
from clock import Clock


class Node(Clock):
    def __init__(self, position: tuple[int, int], range: float) -> None:
        self.id = uuid1()
        Clock.__init__(self)
        self.position = position
        self.range = range
        self.active = True
        self.confidence = 1

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"Node \033[31m{self.id}\033[39m at coordinates {self.position} with time {self.time}.\n"
    
    def move_to(self, new_position: tuple[int, int]) -> None:
        self.position = new_position

    def turn_off(self) -> None:
        if (self.active == True):
            self.active = False
        else:
            print(f"Node \033[31m{self.id}\033[39m is already off.\n")

    def turn_on(self) -> None:
        if (self.active == False):
            self.active = True
        else:
            print(f"Node \033[31m{self.id}\033[39m is already on.\n")

    def in_range(self, position: tuple[float, float]) -> bool:
        x,y = position
        distance = sqrt((self.position[0] - x)**2 + (self.position[1]-y)**2)
        if distance < self.range:
            return True
        else:
            return False

            
if __name__ == "__main__":
    #Test code for current class
    exampleNode = Node((0,0), 1)
    exampleNode.turn_on()
    exampleNode2 = Node((1,1), 1)
    print(exampleNode2)