##########################
# Math380 Final Project 
# Model Exploration 
########################## 

#%% import pyplot
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#%% PRODUCTION 

start_OP = 5964297
start_RP = 2120823.171

#%%
# actual: OP growth > RP growth & OP's i-factor < RP's i-factor
OP = [start_OP]
RP = [start_RP]
n = np.arange(31)
# growth factor of oil production  
a = 0.1372710762

# growth factoer of renewable energy production
b = 0.041262958

# interaction factor of OP and RP for OP
c = -0.0000000399281668

# interaction factor of OP and RP for RP 
d = -0.00000001586660302

for i in range(30):
    OP.append(((1+a)*OP[i]) + (c*OP[i]*RP[i]))
    RP.append(((1+b)*RP[i]) + (d*OP[i]*RP[i]))

data = {'years': n, 'Oil': OP, 'Renewable Energy': RP}
df = pd.DataFrame(data=data)
print(df) 


#create array for n years
n = np.arange(31)
i = 0

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OP, color="b", label="Oil Production Amount")
ax.scatter(n, RP, color="r", label="Renewable Energy Production Amount")
plt.title("Production (Case 1)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OP),max(RP))])
plt.show() 


#%% 
# case 2: OP growth > RP growth & OP's i-factor > RP's i-factor 

OP = [start_OP]
RP = [start_RP]
n = np.arange(31)
# growth factor of oil production  
a = 0.15

# growth factor of renewable energy production
b = 0.05

# interaction factor of OP and RP 
c = -0.000000015

# interaction factor of OP and RP 
d = -0.000000040 

for i in range(30):
    OP.append(((1+a)*OP[i]) + (c*OP[i]*RP[i]))
    RP.append(((1+b)*RP[i]) + (d*OP[i]*RP[i]))

data = {'years': n, 'Oil': OP, 'Renewable Energy': RP}
df = pd.DataFrame(data=data)
print(df) 


#create array for n years
n = np.arange(31)
i = 0

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OP, color="b", label="Oil Production Amount")
ax.scatter(n, RP, color="r", label="Renewable Energy Production Amount")
plt.title("Production (Case 2)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OP),max(RP))])
plt.show() 


#%% 
# case 3: OP growth < RP growth & OP's i-factor < RP's i-factor 

OP = [start_OP]
RP = [start_RP]
n = np.arange(31)
# growth factor of oil production  
a = 0.05

# growth factor of renewable energy production
b = 0.15

# interaction factor of OP and RP 
c = -0.000000040

# interaction factor of OP and RP 
d = -0.000000015 

for i in range(30):
    OP.append(((1+a)*OP[i]) + (c*OP[i]*RP[i]))
    RP.append(((1+b)*RP[i]) + (d*OP[i]*RP[i]))

data = {'years': n, 'Oil': OP, 'Renewable Energy': RP}
df = pd.DataFrame(data=data)
print(df) 


#create array for n years
n = np.arange(31)
i = 0

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OP, color="b", label="Oil Production Amount")
ax.scatter(n, RP, color="r", label="Renewable Energy Production Amount")
plt.title("Production (Case 3)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OP),max(RP))])
plt.show() 

#%%
# case 4: OP growth < RP growth & OP's i-factor > RP's i-factor 

OP = [start_OP]
RP = [start_RP]
n = np.arange(31)
# growth factor of oil production  
a = 0.05

# growth factor of renewable energy production
b = 0.15

# interaction factor of OP and RP 
c = -0.000000015

# interaction factor of OP and RP 
d = -0.000000040 

for i in range(30):
    OP.append(((1+a)*OP[i]) + (c*OP[i]*RP[i]))
    RP.append(((1+b)*RP[i]) + (d*OP[i]*RP[i]))

data = {'years': n, 'Oil': OP, 'Renewable Energy': RP}
df = pd.DataFrame(data=data)
print(df) 


#create array for n years
n = np.arange(31)
i = 0

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OP, color="b", label="Oil Production Amount")
ax.scatter(n, RP, color="r", label="Renewable Energy Production Amount")
plt.title("Production  (Case 4)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OP),max(RP))])
plt.show() 

#%%
# case 5: OP growth < RP growth & OP's i-factor > RP's i-factor 

OP = [start_OP]
RP = [start_RP]
n = np.arange(31)
# growth factor of oil production  
a = 0.05

# growth factor of renewable energy production
b = 0.05

# interaction factor of OP and RP 
c = -0.000000030 

# interaction factor of OP and RP 
d = -0.000000030 

for i in range(30):
    OP.append(((1+a)*OP[i]) + (c*OP[i]*RP[i]))
    RP.append(((1+b)*RP[i]) + (d*OP[i]*RP[i]))

data = {'years': n, 'Oil': OP, 'Renewable Energy': RP}
df = pd.DataFrame(data=data)
print(df) 


#create array for n years
n = np.arange(31)
i = 0

#plot actual data and modeled data on the same graph to compare
ax = plt.gca()

ax.scatter(n, OP, color="b", label="Oil Production Amount")
ax.scatter(n, RP, color="r", label="Renewable Energy Production Amount")
plt.title("Production (Case 5)")
plt.xlabel("Year n since 2020")
plt.ylabel("Thousand Barrels/day")
plt.legend(loc="upper left")
ax.set_ylim([0, max(max(OP),max(RP))])
plt.show() 