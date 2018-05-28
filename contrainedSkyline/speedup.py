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

# with open('speedup_1.txt') as infile:
#     trend_1 = numpy.loadtxt(infile)
    # print trend


# y_max = max(trend[:,1])
#plt.ylim([0, 2])

#plt.plot(trend[:,0], trend[:,1], 'b^-', label='Varying graph size', ms=15, lw=5)
#plt.plot(trend_1[:,0], trend_1[:,1], 'ro-', label='Varying # of object', ms=15, lw=5)
#serial = 2449436.627
# plt.plot(trend[:,0], trend[:,1], 'ro-', label='ExactAlg-baseline', ms=18, lw=5)
# plt.plot(trend[:,0], trend[:,1], 'ro-', label='ExactAlg-improved', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,1], c='r',marker=".",ls="solid",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,1], 'b.', ls="--",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,3], 'b.', ls="solid",label='Approx-range-indexed', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], 'gx-', label='Approx-minPath', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,5], c='k', marker="s",ls="solid",label='Approx-mix', ms=10, lw=4)
# plt.plot(trend[:,0], trend[:,3], c='k', marker="s",ls="--",label='Approx-mix-index', ms=10, lw=4)
#plt.plot(trend[:,0], trend[:,0], 'ro-', ms=10, lw=4, label='Ideal parallel algorithm')
# plt.plot(trend[:,0], serial/trend[:,1], 'b^-', ms=10, lw=4, label='Perfect')
# plt.xlabel('|D|/N ', **axis_font)
# plt.xlabel('average degree of the graph ', **axis_font)

# speedup
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='*', ls="--",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='g', marker ='*', ls="solid",label='Approx-range-indexed', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,4], c='k', marker="d",ls="solid",label='Approx-mix', ms=15, lw=4)
# plt.plot(trend[:,0], trend[:,5], c='k', marker="d",ls="--",label='Approx-mix-indexed', ms=15, lw=4)
# plt.ylabel('Running Time in (Sec.)', **axis_font)
# plt.xlabel('# of graph nodes (in thousands) ', **axis_font)
# plt.legend(loc=2)
# plt.savefig('speedup.pdf', bbox_inches='tight')


# speedup wit improved exact
# plt.plot(trend[:,0], trend[:,1], c='r', marker ='o', ls="-",label='ExactAlg-improved', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='g', marker ='*', ls="--",label='Approx-range', ms=18, lw=4)
# plt.ylabel('Running Time in (Sec.)', **axis_font)
# plt.xlabel('# of graph nodes (in thousands) ', **axis_font)
# plt.legend(loc=2)
# plt.savefig('speedup.pdf', bbox_inches='tight')


#frequency
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='*', ls="--",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls="solid",label='Approx-mix', ms=15, lw=4)
# plt.xlabel('# of graph nodes (in thousands) ', **axis_font)
# plt.ylabel('frequency of skyline checking', **axis_font)
# plt.legend(loc=1)
# plt.savefig('speedup.pdf', bbox_inches='tight')


#frequency with improved exact
# plt.plot(trend[:,0], trend[:,1], c='r', marker ='o', ls="-",label='ExactAlg-improved', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls="solid",label='Approx-mix', ms=15, lw=4)
# plt.xlabel('# of graph nodes (in thousands) ', **axis_font)
# plt.ylabel('frequency of skyline checking', **axis_font)
# plt.legend(loc=2)
# plt.savefig('speedup.pdf', bbox_inches='tight')

# goodness
plt.plot(trend[:,0], trend[:,1], c='g', marker ='*', ls="--",label='Approx-range', ms=18, lw=4)
plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls="solid",label='Approx-mix', ms=15, lw=4)
plt.ylabel('Goodness', **axis_font)
plt.xlabel('# of graph node (in thousands) ', **axis_font)
plt.legend(loc=1)
plt.savefig('goodness.pdf', bbox_inches='tight')


# goodness top 10
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='*', ls="-.",label='Approx-range_top10', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls="-.",label='Approx-mix_top10', ms=15, lw=4)
# plt.ylabel('Goodness', **axis_font)
# plt.xlabel('# of graph node (in thousands) ', **axis_font)
# plt.legend(loc=1)
# plt.savefig('goodness_top_10.pdf', bbox_inches='tight')


#goodness top 100
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='*', ls=":",label='Approx-range_top100', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls=":",label='Approx-mix_top100', ms=15, lw=4)
# plt.ylabel('Goodness', **axis_font)
# plt.xlabel('# of graph node (in thousands) ', **axis_font)
# plt.legend(loc=4)
# plt.savefig('goodness_top_100.pdf', bbox_inches='tight')


# plt.xlabel('# of graph nodes (in thousands) ', **axis_font)
# plt.ylabel('Visited Ratio', **axis_font)


# plt.savefig('speedup.pdf', bbox_inches='tight')
# plt.show()

