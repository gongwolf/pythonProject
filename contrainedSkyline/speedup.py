import numpy
import scipy
import sklearn.preprocessing
import matplotlib.pyplot as plt
import matplotlib
from pylab import *
import os
import json

font = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 25}
matplotlib.rc('font', **font)
axis_font = {'fontname':'Arial', 'size':'35'}

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

with open('speedup.txt') as infile:
    trend = numpy.loadtxt(infile)
    print trend
# y_max = max(trend[:,1])
#plt.ylim([0, 2])

#serial = 2449436.627
plt.plot(trend[:,0], trend[:,2], 'b^-', label='ExactAlg-baseline', ms=10, lw=4)
plt.plot(trend[:,0], trend[:,1], 'ro-', label='ExactAlg-improved', ms=10, lw=4)
#plt.plot(trend[:,0], trend[:,0], 'ro-', ms=10, lw=4, label='Ideal parallel algorithm')
# plt.plot(trend[:,0], serial/trend[:,1], 'b^-', ms=10, lw=4, label='Perfect')
plt.xlabel('#k of Graph with 300 objects', **axis_font)
plt.ylabel('Times to checking Skyline', **axis_font)
plt.legend()

plt.savefig('speedup.pdf', bbox_inches='tight')
# plt.show()

