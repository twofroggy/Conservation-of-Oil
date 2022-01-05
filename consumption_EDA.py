##########################
# Math380 Final Project 
# Model Exploration 
########################## 

#%% import pyplot
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#%% CONSUMPTION 

# using 2020's data for this!!! 
start_OC = 5805959.921
start_RC = 3573412.701

#%% stability analysis starting points (switched the ones from above)
start_RC = 5805959.921
start_OC = 3573412.701

#%%
# case 1: OC growth > RC growth & OC's i-factor < RC's i-factor
OC = [start_OC]
RC = [start_RC]
n = np.arange(41) #until 2060!!!

# growth factor of oil consumption  
a = 0.020

# growth factoer of renewable energy consumption
b = -0.006

# interaction factor of OC and RC for OC 
c = -0.000000044

# interaction factor of OC and RC for RC 
d = -0.000000014

for i in range(40):
    OC.append(((1+a)*OC[i]) + (c*OC[i]*RC[i]))
    RC.append(((1+b)*RC[i]) + (d*OC[i]*RC[i]))

data = {'years': n, 'Oil': OC, 'Renewable Energy': RC}
df = pd.DataFrame(data=data)
print(df) 
df.to_csv(r'/Users/tiffwong/Desktop/math380/final project/consumption_case1.csv', index = False)

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OC, color="b", label="Oil Consumption Amount")
ax.scatter(n, RC, color="r", label="Renewable Energy Consumption Amount")
plt.title("Consumption (Case 1)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OC),max(RC))])
plt.show() 

#%%
# case 2: OC growth > RC growth & OC's i-factor > RC's i-factor
OC = [start_OC]
RC = [start_RC]
n = np.arange(41) #until 2060!!!

# growth factor of oil consumption  
a = 0.020

# growth factoer of renewable energy consumption
b = -0.006

# interaction factor of OC and RC for OC 
c = -0.000000014

# interaction factor of OC and RC for RC 
d = -0.000000044

for i in range(40):
    OC.append(((1+a)*OC[i]) + (c*OC[i]*RC[i]))
    RC.append(((1+b)*RC[i]) + (d*OC[i]*RC[i]))

data = {'years': n, 'Oil': OC, 'Renewable Energy': RC}
df = pd.DataFrame(data=data)
print(df) 
df.to_csv(r'/Users/tiffwong/Desktop/math380/final project/consumption_case2.csv', index = False)

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OC, color="b", label="Oil Consumption Amount")
ax.scatter(n, RC, color="r", label="Renewable Energy Consumption Amount")
plt.title("Consumption (Case 2)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OC),max(RC))])
plt.show() 

#%%
# actual (case 3): OC growth < RC growth & OC's i-factor < RC's i-factor
OC = [start_OC]
RC = [start_RC]
n = np.arange(41)
# growth factor of oil consumption  
a = -0.006012076354 

# growth factoer of renewable energy consumption
b = 0.020247218

# interaction factor of OC and RC for OC 
c = -0.00000004382777105

# interaction factor of OC and RC for RC 
d = -0.00000001382597676

for i in range(40):
    OC.append(((1+a)*OC[i]) + (c*OC[i]*RC[i]))
    RC.append(((1+b)*RC[i]) + (d*OC[i]*RC[i]))

data = {'years': n, 'Oil': OC, 'Renewable Energy': RC}
df = pd.DataFrame(data=data)
print(df) 
df.to_csv(r'/Users/tiffwong/Desktop/math380/final project/consumption_case3.csv', index = False)

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OC, color="b", label="Oil Consumption Amount")
ax.scatter(n, RC, color="r", label="Renewable Energy Consumption Amount")
plt.title("Consumption (Case 3)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OC),max(RC))])
plt.show() 


#%%
# case 4: OC growth < RC growth & OC's i-factor > RC's i-factor
OC = [start_OC]
RC = [start_RC]
n = np.arange(41)
# growth factor of oil consumption  
a = -0.006012076354 

# growth factoer of renewable energy consumption
b = 0.020247218

# interaction factor of OC and RC for OC 
c = -0.000000014

# interaction factor of OC and RC for RC 
d = -0.000000044



for i in range(40):
    OC.append(((1+a)*OC[i]) + (c*OC[i]*RC[i]))
    RC.append(((1+b)*RC[i]) + (d*OC[i]*RC[i]))

data = {'years': n, 'Oil': OC, 'Renewable Energy': RC}
df = pd.DataFrame(data=data)
print(df) 
df.to_csv(r'/Users/tiffwong/Desktop/math380/final project/consumption_case4.csv', index = False)

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OC, color="b", label="Oil Consumption Amount")
ax.scatter(n, RC, color="r", label="Renewable Energy Consumption Amount")
plt.title("Consumption  (Case 4)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OC),max(RC))])
plt.show() 

#%%
# case 5: OC growth = RC growth & OC's i-factor > RC's i-factor
OC = [start_OC]
RC = [start_RC]
n = np.arange(41) #until 2060!!!

# growth factor of oil consumption  
a = 0.020

# growth factoer of renewable energy consumption
b = 0.020

# interaction factor of OC and RC for OC 
c = -0.000000014

# interaction factor of OC and RC for RC 
d = -0.000000044

for i in range(40):
    OC.append(((1+a)*OC[i]) + (c*OC[i]*RC[i]))
    RC.append(((1+b)*RC[i]) + (d*OC[i]*RC[i]))

data = {'years': n, 'Oil': OC, 'Renewable Energy': RC}
df = pd.DataFrame(data=data)
print(df) 
df.to_csv(r'/Users/tiffwong/Desktop/math380/final project/consumption_case5.csv', index = False)


#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OC, color="b", label="Oil Consumption Amount")
ax.scatter(n, RC, color="r", label="Renewable Energy Consumption Amount")
plt.title("Consumption (Case 5)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OC),max(RC))])
plt.show() 