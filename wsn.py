"""
Module for class WirelessSensorNetwork.
"""
from random import randint
from node import Node

class WirelessSensorNetwork:
    """
    Class for simulating wireless sensor networks and providing methods
    for various setups and calculations inside the network.
    """
    def __init__(self, size: tuple[int, int], node_amount: int, trasmission_range: int) -> None:
        self.size = size
        self.node_amount = node_amount
        node_positions = self._generate_positions()
        self.network = []
        for position in node_positions:
            self.network.append(Node(position, trasmission_range))

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.network}"

    def _generate_positions(self) -> set:
        positions = set()
        while len(positions) < self.node_amount:
            x_position = randint(0, self.size[0]-1)
            y_position = randint(0, self.size[1]-1)
            positions.add((x_position, y_position))
        return list(positions)

    def init_clocks(self) -> None:
        """
        Initialise the clock of all nodes according to set random parameters.
        """
        for node in self.network:
            node.scramble_time(randint(-100,100)/10000, randint(-1500,1500))

    def pass_time(self, passed_ticks) -> None:
        """
        Advance the clock of all nodes by the amount of passed ticks.
        """
        for node in self.network:
            node.pass_time(passed_ticks)

    def draw_network(self) -> None:
        """
        Draw the network rectangle in the console. * for empty, N for node.
        """
        network_canvas = [['*' for i in range(self.size[0])] for j in range(self.size[0])]
        for node in self.network:
            network_canvas[node.position[1]][node.position[0]] = 'N'
        for row in network_canvas:
            print(row)

    def average_time(self) -> float:
        """
        Calculate average time in the network.
        """
        time_sum = 0
        for node in self.network:
            time_sum += node.time
        average_network_time = time_sum / self.node_amount
        return average_network_time

    def mean_internal_error(self) -> float:
        """
        Calculate the average error of all nodes in comparison to average time.
        """
        average_network_time = self.average_time()
        error_sum = 0
        for node in self.network:
            error_sum += average_network_time - node.time
        average_internal_error = error_sum / self.node_amount
        return average_internal_error

if __name__ == "__main__":
    #Test code for class WirelessSensorNetwork
    wsn = WirelessSensorNetwork((5, 5), 8, 4)
    print(wsn)
    wsn.draw_network()
    