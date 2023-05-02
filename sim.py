from matplotlib import pyplot
from wsn import WirelessSensorNetwork
from ccs import ConsensusClockSynchronization

if __name__ == "__main__":
    simulation = WirelessSensorNetwork((10,10), 100, 3)
    system_time = 0
    #simulation = WirelessSensorNetwork((2,2), 4)
    ccs = ConsensusClockSynchronization(simulation)

    simulation.init_clocks()
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
    ccs.synchronize(simulation)
    print(f"Mean internal error {simulation.mean_internal_error()}, \
          average time {simulation.average_time()}")
    for node in simulation.network:
        print(f"{node.natural_skew} vs {node.compensation_skew} and {node.time}")
