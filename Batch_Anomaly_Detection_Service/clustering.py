import logging 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
plt.rcParams.update({font.size: 22}) # matplotlib config to update font size to 22 as default 
import datetime 
from numpy.random import MT19937 # MT19937 (Mersenne Twister algorithm) is a random number generator 

# SeedSequence ensures reproducibility 
from numpy.random import RandomState, SeedSequence # RandomState provides a way to set a state so that you can reproduce the same sequence of random numbers every time you run the code.
rs = RandomState(MT19937(SeedSequence(123456789))) # rs can now be used to generate random numbers with controlled randomness 


def simulate_ride_distances(): # This function simulates ride distances 
    logging.info('Simulating ride distances...')
    ride_dists = np.concatenate(
        (
            10 * np.random.random(size=370),
            30 * np.random.random(size=10),
            10 * np.random.random(size=10),
            10 * np.random.random(size=10),
        )
    )
    return ride_dists

def simulate_ride_speeds():
    logging.info('Simulating ride speeds...')
    ride_speeds = np.concatenate(
        (
            np.random.normal(loc=30, scale=5, size=370),
            np.random.normal(loc=30, scale=5, size=10),  # same speed
            np.random.normal(loc=50, scale=10, size=10),  # high speed
            np.random.normal(loc=15, scale=4, size=10)  # low speed
        )
    )
    return ride_speeds