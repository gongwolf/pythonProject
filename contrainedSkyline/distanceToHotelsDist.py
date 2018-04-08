import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_file = "/home/gqxwolf/mydata/pythonProject/hotels_distance.dat"

with open(data_file) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]


dist_list=[i for i in range( int(content[-1].split(" ")[0])+1 )]
num_count=np.zeros(len(dist_list))

#print content[-1]

for line in  content:
    d_num = int(line.split(" ")[0])
    counter = int(line.split(" ")[-1])
    num_count[d_num]=counter



#print len(num_count)
#print len(dist_list)

def plot_bar():
    index = np.arange(len(dist_list))
    plt.bar(index,num_count)
    plt.show()


plot_bar()
