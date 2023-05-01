"""Mode for class ConsensusClockSynchronization."""
from random import shuffle
from wsn import WirelessSensorNetwork
from node import Node

class ConsensusClockSynchronization(): # pylint: disable=too-few-public-methods
    """Class for clock synchronization inside a wireless sensor 
    network using the consensus clock synhronization algorithm."""
    def __init__(self, simulation: WirelessSensorNetwork) -> None:
        self.parameters = {}
        for node in simulation.network:
            # Set initial synchronization time [0] and confidence factor [1]
            self.parameters[node.id] = [node.time, 1]

    def synchronize(self, simulation: WirelessSensorNetwork) -> None:
        """Perform the consensus clock synhronization algorithm on the simulation."""
        # Reset all confidence factors
        for node in simulation.network:
            self.parameters[node.id][1] = 1
        # All nodes send synchronization messages in random order
        shuffle(simulation.network)
        for sending_node in simulation.network:
            for receiving_node in simulation.network:
                if sending_node.in_range(receiving_node.position, receiving_node.id) is True:
                    old_time = receiving_node.time
                    self._offset_compensation(sending_node, receiving_node)
                    self._skew_compensation(receiving_node, old_time)
        for node in simulation.network:
            # Store current time for furute skew compensation
            self.parameters[node.id][0] = node.time


    def _offset_compensation(self, sender:Node, receiver: Node) -> None:
        sender_confidence = self.parameters[sender.id][1]
        receiver_confidence = self.parameters[receiver.id][1]
        confidence_factor = sender_confidence / (receiver_confidence + sender_confidence)
        # CCS formula (9)
        receiver.time = receiver.time + confidence_factor * (sender.time - receiver.time)
        # Increase confidence factor of receiver
        self.parameters[receiver.id][1] += 1

    def _skew_compensation(self, receiver: Node, old_time: float) -> None:
        last_synchronization = self.parameters[receiver.id][0]
        new_time = receiver.time
        time_difference = (old_time - last_synchronization)/(new_time - last_synchronization)
        # CCS formula (16)
        receiver.compensation_skew = receiver.compensation_skew * time_difference

if __name__ == "__main__":
    # Test code for class WirelessSensorNetwork
    test = WirelessSensorNetwork((2, 2), 4)
    ccs = ConsensusClockSynchronization(test)
    test.network[0].time = 1
    test.network[1].time = 2
    test.network[2].time = 4
    test.network[3].time = 5
    ccs.synchronize(test)
    print(f"Average time: {test.average_time()}\n")
