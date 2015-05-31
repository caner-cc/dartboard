# numpy and matplotlib libraries for plotting
import numpy as np
import matplotlib.pyplot as plt

# array of the cos values of each vector from the excel file:
cosList = [1,0.9510565163,0.8090169944,0.5877852523,0.3090169944,
0,-0.3090169944,-0.5877852523,-0.8090169944,-0.9510565163,
-1,-0.9510565163,-0.8090169944,-0.5877852523,-0.3090169944,
0,0.3090169944,0.5877852523,0.8090169944,0.9510565163]

# array of the sin values of each vector from the excel file:
sinList = [0,0.3090169944,0.5877852523,0.8090169944,0.9510565163,
1,0.9510565163,0.8090169944,0.5877852523,0.3090169944,
0,-0.3090169944,-0.5877852523,-0.8090169944,-0.9510565163,
-1,-0.9510565163,-0.8090169944,-0.5877852523,-0.3090169944]

# array of magnitude values from the excel file
# ******** REARRANGE THIS LIST TO REARRANGE PLOTTED VECTORS *********
magList = [4,12,11,18,1,20,5,10,9,15,6,8,16,7,19,3,17,2,14,13]

# create an empty list
soa  = []

# create 20 zero vectors in 4 space because the untweaked plotting
# code we got from the internet takes 4 space vectors
for i in range(20):
    soa.append([0,0,0,0])
    
# Turn the array we made into a ndarray that the numpy library provides
# Again, because the plotting code is making use of the numpy library
soa = np.array(soa)

# uncomment the next statement to make sure your vectors look okay
#print(soa)

# Fill the zero vectors with actual magnitudes multiplied with the x
# and y components of the vectors
for i in range(20):
    soa[i][2] = magList[i] * cosList[i]
    soa[i][3] = magList[i] * sinList[i]
    
# uncomment the next statement to make sure your vectors look okay
#print(soa);

# vector plotting code I got from the internet. works on 4 space vectors
X,Y,U,V = zip(*soa)
plt.figure()
ax = plt.gca()
ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
ax.set_xlim([-20,20])
ax.set_ylim([-20,20])
plt.draw()
plt.show()
