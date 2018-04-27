from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_file = "/home/gqxwolf/mydata/pythonProject/hotels_distance.dat"

with open(data_file) as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]


dist_list=[i for i in range( int(content[-1].split(" ")[0])+1 )]

sum=0
for i in content:
    sum = sum + int(i.split(" ")[1])
print "total ",sum
num_count=np.zeros(len(dist_list))

#print content[-1]

Expectation = 0;

for line in  content:
    d_num = int(line.split(" ")[0])
    counter = int(line.split(" ")[-1])
    num_count[d_num]=counter/sum
    Expectation = Expectation+d_num*num_count[d_num]


#print len(num_count)
#print len(dist_list)

def plot_bar():
    index = np.arange(len(dist_list))
    plt.bar(index,num_count,width=1.0,align="edge",linewidth="1",edgecolor="k")
    ax = plt.gca()
    #plt.text(0.05, 20, r'Expected Value = 4.212033487',fontsize=20)
    plt.xlim(0,len(dist_list))
    plt.ylabel("Probability")
    plt.xlabel("Number of Bus Stops within a certain range")

    textstr = 'Expected Value = '+ str(Expectation)

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # place a text box in upper left in axes coords
    ax.text(0.50, 0.95, textstr, transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=props)

    plt.show()


plot_bar()
