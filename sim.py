"""
Module for simulation of consensus clock synhronization inside a wireless
sensor network. The simulation is meant to work in milliseconds.
"""
from sim_input import parse_input
from wsn import WirelessSensorNetwork
from ccs import initialise_ccs
from ccs import concensus_clock_synhronization

if __name__ == "__main__":
    input_data = parse_input("test.txt")
    simulation = WirelessSensorNetwork(input_data)
    # System time should be in milliseconds.
    initialise_ccs(simulation)

    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
#     for node in simulation.network:
#         print(f"{node.natural_skew} vs {node.compensation_skew} and {node.time/1000:.2f}")
    simulation.pass_time(600000)
    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
    concensus_clock_synhronization(simulation)
    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
#     for node in simulation.network:
#         print(f"{node.natural_skew} vs {node.compensation_skew} and {node.time/1000:.2f}")
                