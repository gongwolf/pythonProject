import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

node_f_name = "/home/gqxwolf/mydata/projectData/testGraph100_1/data/NodeInfo.txt"
seg_f_name = "/home/gqxwolf/mydata/projectData/testGraph100_1/data/SegInfo.txt"

node_data = pd.read_csv(node_f_name, sep=" ", header=None)
seg_data = pd.read_csv(seg_f_name, sep=" ", header=None)


plt.plot(node_data[1], node_data[2],"ro", markersize="4")

#for seg in seg_data:
for index,row in seg_data.iterrows():
    print row[0],row[1]
    x=[node_data.loc[row[0]][1],node_data.loc[row[0]][2]]
    y=[node_data.loc[row[1]][1],node_data.loc[row[1]][2]]
    plt.arrow(x[0],x[1],y[0]-x[0],y[1]-x[1],fc="k", ec="k",head_width=2, head_length=2 )
    # print y


plt.show()