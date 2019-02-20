
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
a = np.sqrt(2)
b = 1.414213562373095

rang = range(1, 100)
res = [(np.power(a, i)-np.power(b, i),i)
       for i in rang if np.power(a, i)-np.power(b, i)<1e-6]
print(a,res)
plt.figure()
plt.plot(res[:,1],res[:,0])
plt.show()
