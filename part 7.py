import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.0,3.0,0.01)
y=np.sin(2*np.pi*x)
y2=np.cos(2*np.pi*x)
y3=np.tan(2*np.pi*x)
# y4=np.intersect1d(2*np.pi*x)

plt.plot(x,y,label="line1")
plt.plot(x,y2)
# plt.plot(x,y3)
# plt.plot(x,y4)

plt.xlabel("kush")
plt.ylabel("love")
plt.grid()
plt.show()