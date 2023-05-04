"""
Module for algorithm fro consensus clock synhronization.
The module must first be initialised.
"""
from random import shuffle
from wsn import WirelessSensorNetwork
from node import Node

ccs_parameters = {}

def initialise_ccs(simulation: WirelessSensorNetwork) -> None:
    """
    Set initial last synchronization time as current and set confidence to 1.
    """
    for node in simulation.network:
        # Set initial synchronization time [0] and confidence factor [1]
        ccs_parameters[node.uid] = [node.time, 1]

def concensus_clock_synhronization(simulation: WirelessSensorNetwork) -> None:
    """
    Perform the consensus clock synhronization algorithm on
    a given network, that was previously initialised.
    """
    # Reset all confidence factors
    for node in simulation.network:
        ccs_parameters[node.uid][1] = 1
    # All nodes send synchronization messages in random order
    shuffle(simulation.network)
    for sender_node in simulation.network:
        if sender_node.active is True:
            for receiver_node in simulation.network:
                if receiver_node.active is True:
                    if sender_node.in_range(receiver_node.position, receiver_node.uid) is True:
                        old_time = receiver_node.time
                        _offset_compensation(sender_node, receiver_node)
                        _skew_compensation(receiver_node, old_time)
    for node in simulation.network:
        # Store current time for furute skew compensation
        ccs_parameters[node.uid][0] = node.time


def _offset_compensation(sender:Node, receiver: Node) -> None:
    sender_confidence = ccs_parameters[sender.uid][1]
    receiver_confidence = ccs_parameters[receiver.uid][1]
    confidence_factor = sender_confidence / (receiver_confidence + sender_confidence)
    # CCS formula (9)
    receiver.time = receiver.time + confidence_factor * (sender.time - receiver.time)
    # Increase confidence factor of receiver
    ccs_parameters[receiver.uid][1] += 1

def _skew_compensation(receiver: Node, old_time: float) -> None:
    last_synchronization = ccs_parameters[receiver.uid][0]
    new_time = receiver.time
    time_difference = (old_time - last_synchronization)/(new_time - last_synchronization)
    # CCS formula (16)
    receiver.compensation_skew = receiver.compensation_skew * time_difference

if __name__ == "__main__":
    # Test code for module ccs
    pass
    # test = WirelessSensorNetwork((2, 2), 4, 3)
    # initialise_ccs(test)
    # test.network[0].time = 1
    # test.network[1].time = 2
    # test.network[2].time = 4
    # test.network[3].time = 5
    # concensus_clock_synhronization(test)
    # print(f"Average time: {test.average_time()}\n")
