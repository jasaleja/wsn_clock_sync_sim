"""
Module for simulation of consensus clock synhronization inside a wireless
sensor network. The simulation is meant to work in milliseconds.
"""
import matplotlib.pyplot as plt
from sim_input import parse_input
from wsn import WirelessSensorNetwork
from ccs import initialise_ccs
from ccs import consensus_clock_synhronization

if __name__ == "__main__":
    input_data = parse_input("test.txt")
    simulation = WirelessSensorNetwork(input_data)

    
    average_network_time = [simulation.average_time()/1000]
    real_time = [0]

    
    # System time should be in milliseconds.
    initialise_ccs(simulation)

    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
#     for node in simulation.network:
#         print(f"{node.natural_skew} vs {node.compensation_skew} and {node.time/1000:.2f}")
    for i in range(100):
        simulation.pass_time(100000)
        consensus_clock_synhronization(simulation)
        average_network_time.append(simulation.average_time()/1000)
        real_time.append(i*100)
        
    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
    
    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
    
    plt.plot(average_network_time, real_time)
    plt.xlabel('Time')
    plt.ylabel('Network Time')
    plt.title("Real time vs Network time")
    plt.show()
#     for node in simulation.network:
#         print(f"{node.natural_skew} vs {node.compensation_skew} and {node.time/1000:.2f}")
                