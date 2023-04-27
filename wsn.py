from random import randint
from node import Node

class WirelessSensorNetwork:
    def __init__(self, size: tuple[int, int], number_of_nodes: int) -> None:
        self.size = size
        self.number_of_nodes = number_of_nodes
        node_positions = self._generate_positions()
        self.network = list()
        for position in node_positions:
            self.network.append(Node(position, randint(1, self.size[0]-1)))

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"{self.network}"
    
    def _generate_positions(self) -> set:
        positions = set()
        while len(positions) < self.number_of_nodes:
            x = randint(0, self.size[0]-1)
            y = randint(0, self.size[1]-1)
            positions.add((x, y))
        return list(positions)
    
    def pass_time(self, passed_ticks) -> None:
        pass

    def draw_network(self) -> None:
        network_canvas = [['*' for i in range(self.size[0])] for j in range(self.size[0])]
        for node in self.network:
            network_canvas[node.position[1]][node.position[0]] = 'N'
        for row in network_canvas:
            print(row)


if __name__ == "__main__":
    wsn = WirelessSensorNetwork((5, 5), 8)
    print(wsn)
    wsn.draw_network()