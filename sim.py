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
    system_time = 0
    initialise_ccs(simulation)

    print(f"Mean internal error {simulation.mean_internal_error()}, \
          average time {simulation.average_time()}")
    for node in simulation.network:
        print(f"{node.natural_skew} vs {node.compensation_skew} and {node.time}")
    
    simulation.pass_time(600000)
    print(f"Mean internal error {simulation.mean_internal_error()}, \
          average time {simulation.average_time()}")
    # while True:
    #     simulation.pass_time(1)
    #     x.append(system_time+1)
    #     y.append(simulation.mean_internal_error())
    #     if system_time%2 == 0:
    #         ccs.synchronize(simulation)
    #     system_time += 1
    #     if (system_time == 100):
    #         break
    concensus_clock_synhronization(simulation)
    print(f"Mean internal error {simulation.mean_internal_error()}, \
          average time {simulation.average_time()}")
    for node in simulation.network:
        print(f"{node.natural_skew} vs {node.compensation_skew} and {node.time}")
                