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