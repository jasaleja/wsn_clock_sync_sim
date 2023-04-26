from clock import Clock
from uuid import uuid1

class Node(Clock):
    def __init__(self, position: tuple[float, float], range: float) -> None:
        self.id = uuid1()
        Clock.__init__(self)
        self.x, self.y = position
        self.range = range
        self.active = True
        self.confidence = 0

    def moveTo(self, newPosition: tuple[float, float]) -> None:
        self.x, self.y = newPosition

    def turnOff(self) -> None:
        if (self.active == True):
            self.active = False
        else:
            print("Node is already off.")

    def turnOn(self) -> None:
        if (self.active == False):
            self.active = True
        else:
            print("Node is already on.")

            
if __name__ == "__main__":
    exampleNode = Node((0,0), 1)
    print(exampleNode.id)
    exampleNode2 = Node((1,1), 1)
    print(exampleNode2.id)