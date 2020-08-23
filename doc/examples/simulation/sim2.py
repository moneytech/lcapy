from lcapy import *
import numpy as np

a = Circuit("""
V1 1 0 step 10; down
R1 1 2 5; right
C1 2 0_2 0.01; down
W 0 0_2; right""")

tv = np.linspace(0, 1, 200)

sim = a.sim
results = sim(tv)

ax = a.R1.v.plot(tv)
ax.plot(tv, results.R1.v)
