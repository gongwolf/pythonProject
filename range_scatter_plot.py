import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#read data
my_data =pd.read_csv("data.csv",header=None)
x=my_data[0]
y=my_data[1]

plt.scatter(x, y,marker='.')
#plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')

northing=[456713.071,456717.1654,456718.7758,456735.574,456737.635,456737.797,456738.1461,456736.4407,456719.1844,456713.4275]
easting= [3789861.165,3789856.496,3789856.273,3789854.871,3789858.496,3789859.696,3789863.515,3789865.093,3789866.99,3789866.585]

convex_hull = np.asarray((easting,northing))
num_pair = convex_hull.shape[1]
print num_pair

x=convex_hull[1]
y=convex_hull[0]

print abs(sum(x[i] * (y[i + 1] - y[i - 1]) for i in xrange(-1, num_pair - 1))) / 2.0

area=0
for i in xrange(num_pair):
	i1=i+1;
	if i1 == num_pair:
		i1=0
	print i,x[i],i+1,y[i1],i-1,y[i-1]
	area += x[i]*(y[i1]-y[i - 1])
area /= 2.0

print area
plt.plot(convex_hull[1],convex_hull[0],'ro')
for i in xrange(num_pair-1):
	plt.plot([convex_hull[1][i],convex_hull[1][i+1]],[convex_hull[0][i],convex_hull[0][i+1]],color='r', linewidth=0.5+i*0.2)
plt.plot([convex_hull[1][-1],convex_hull[1][0]],[convex_hull[0][-1],convex_hull[0][0]],color='r', linewidth=0.5+num_pair*0.2)

plt.show()
