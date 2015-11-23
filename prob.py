import matplotlib.pyplot as plt
import collections
import numpy as np 
import scipy.stats as stats
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
#1. frequencies
c = collections.Counter(x)
# calculate the number of instances in the list
count_sum = sum(c.values())
for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))
#2. boxplot
plt.boxplot(x)
plt.savefig("boxplot.png")
plt.show() # added this show in b/c if not, i get a histogram on top of my box plot
#3. histogram
plt.hist(x, histtype='bar')
plt.savefig("histogram.png")
#4 QQ
plt.figure()
graph1=stats.probplot(x, dist="norm", plot=plt)
plt.savefig("qqn.png")
