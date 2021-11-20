# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:38:47 2021

@author: Michael
"""
import numpy as np
import matplotlib.pyplot as plt
mean_list = [3.4, 3.6, 2.98, 4.88, 5.78, 5.44, 6.08, 7.36, 9.1, 9.56, 5.84, 9.6, 8.8, 8.18, 12.58, 10.8, 10.22, 11.46, 15.6, 16.02, 14.92, 14.18, 16.86, 20.46, 20.54, 23.46]
var_list = [0.35999999999999993, 0.44, 0.05959999999999999, 0.7456, 1.3316000000000003, 0.7663999999999999, 9.673600000000002, 3.5103999999999997, 7.57, 11.566400000000002, 1.4144000000000005, 22.76, 3.4399999999999995, 1.1076000000000001, 26.5636, 8.8, 5.2116, 5.5284, 21.48, 15.3396, 16.3936, 13.107600000000001, 25.1604, 22.328400000000002, 11.0884, 39.08840000000001]




x = np.linspace(15,41,26)


plt.plot(x,mean_list)

plt.title("Average Computing Time with n Nodes")
plt.xlabel('Number of Nodes')
plt.ylabel("Millisecond")
plt.legend()
plt.grid(linestyle = '--', linewidth = 0.5)
plt.savefig("Average Compouting Time.png",dpi = 300)
plt.show()


plt.plot(x,var_list)

plt.title("Average Computing Time Variance with n Nodes")
plt.xlabel('Number of Nodes')
plt.legend()
plt.grid(linestyle = '--', linewidth = 0.5)
plt.savefig("Average Compouting Time Variance.png",dpi = 300)
plt.show()


print(len(mean_list))