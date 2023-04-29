from wsn import WirelessSensorNetwork
from node import Node

def consensus_clock_synchronization(simulation: WirelessSensorNetwork) -> None:
    for node in simulation.network:
        node.confidence = 1
    for sending_node in simulation.network:
        for receiving_node in simulation.network:
            if (sending_node.in_range(receiving_node.position, receiving_node.id) == True):
                _offset_compensation(sending_node, receiving_node)

def _offset_compensation(sender:Node, receiver: Node):
    confidence_factor = sender.confidence / (receiver.confidence + sender.confidence)
    receiver.time = receiver.time + confidence_factor * (sender.time - receiver.time)
    receiver.confidence += 1

if __name__ == "__main__":
    test = WirelessSensorNetwork((2, 2), 4)
    test.network[0].time = 1
    test.network[1].time = 2
    test.network[2].time = 4
    test.network[3].time = 5
    consensus_clock_synchronization(test)
    print(f"Average time: {test.average_time()}\n")