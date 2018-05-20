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
        'size'   : 30}
matplotlib.rc('font', **font)
axis_font = {'fontname':'Arial', 'size':'35'}

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

with open('speedup.txt') as infile:
    trend = numpy.loadtxt(infile)
    # print trend

with open('speedup_1.txt') as infile:
    trend_1 = numpy.loadtxt(infile)
    # print trend


# y_max = max(trend[:,1])
#plt.ylim([0, 2])

#plt.plot(trend[:,0], trend[:,1], 'b^-', label='Varying graph size', ms=15, lw=5)
#plt.plot(trend_1[:,0], trend_1[:,1], 'ro-', label='Varying # of object', ms=15, lw=5)
#serial = 2449436.627
plt.plot(trend[:,0], trend[:,1], 'ro-', label='ExactAlg-baseline', ms=18, lw=5)
# plt.plot(trend[:,0], trend[:,1], 'ro-', label='ExactAlg-improved', ms=18, lw=5)
#plt.plot(trend[:,0], trend[:,0], 'ro-', ms=10, lw=4, label='Ideal parallel algorithm')
# plt.plot(trend[:,0], serial/trend[:,1], 'b^-', ms=10, lw=4, label='Perfect')
plt.xlabel('|D|/N ', **axis_font)
# plt.xlabel('average degree of the graph ', **axis_font)
# plt.ylabel('Running Time in (Sec.)', **axis_font)
# plt.ylabel('frequency of skyline checking', **axis_font)
plt.ylabel('Visited Ratio', **axis_font)

# plt.legend(loc=2)

plt.savefig('speedup.pdf', bbox_inches='tight')
# plt.show()

