"""
Module for simulation of consensus clock synhronization inside a wireless
sensor network. The simulation is meant to work in milliseconds.
"""
import matplotlib.pyplot as plt
import numpy as np
from sim_input import parse_input
from wsn import WirelessSensorNetwork
from ccs import initialise_ccs
from ccs import concensus_clock_synhronization

if __name__ == "__main__":
    input_data = parse_input("test.txt")
    simulation = WirelessSensorNetwork(input_data)
    fig = plt.figure(0)
    ax = plt.axes(projection = "3d")
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
    simulation.pass_time(600000)

    fig = plt.figure(1)
    ax = plt.axes(projection = "3d")
    dz = [abs(simulation.average_time() - node.time) for node in simulation.network]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
    plt.show(block = False)

    # Perform synchronization.
    concensus_clock_synhronization(simulation)

    fig = plt.figure(2)
    ax = plt.axes(projection = "3d")
    dz = [abs(simulation.average_time() - node.time) for node in simulation.network]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
    plt.show()
                