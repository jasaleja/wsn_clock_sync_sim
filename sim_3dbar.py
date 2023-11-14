"""
Module for simulation of consensus clock synchronization inside a wireless
sensor network. The simulation is meant to work in milliseconds.
"""
import matplotlib.pyplot as plt
import numpy as np
from sim_input import parse_input
from wsn import WirelessSensorNetwork
from ccs import initialise_ccs
from ccs import consensus_clock_synchronization

if __name__ == "__main__":
    input_data = parse_input("test.txt")
    simulation = WirelessSensorNetwork(input_data)
    fig = plt.figure(0)
    ax = plt.axes(projection = "3d")
    plt.xlabel('x')
    plt.ylabel('y')
    numOfCols, numOfRows = simulation.size
    xpos = np.arange(0, numOfCols, 1)
    ypos = np.arange(0, numOfRows, 1)
    xpos, ypos = np.meshgrid(xpos, ypos)
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros(numOfCols * numOfRows)
    dx = np.ones(numOfRows * numOfCols)
    dy = np.ones(numOfCols * numOfRows)
    dz = [abs(simulation.average_time() - node.time) for node in simulation.network]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
    plt.show(block = False)

    # System time should be in milliseconds.
    initialise_ccs(simulation)
    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
    simulation.pass_time(600000)
    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
    fig = plt.figure(1)
    ax = plt.axes(projection = "3d")
    plt.xlabel('x')
    plt.ylabel('y')
    dz = [abs(simulation.average_time() - node.time) for node in simulation.network]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
    plt.show(block = False)

    # Perform synchronization.
    consensus_clock_synchronization(simulation)
    print(f"Mean internal error {simulation.mean_error():4.2f}, \
          average time {simulation.average_time()/1000:4.2f}")
    fig = plt.figure(2)
    ax = plt.axes(projection = "3d")
    plt.xlabel('x')
    plt.ylabel('y')
    dz = [abs(simulation.average_time() - node.time) for node in simulation.network]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
    plt.show()
                