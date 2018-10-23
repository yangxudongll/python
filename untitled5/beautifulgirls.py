import matplotlib.pyplot as plt
import numpy as np
import math
import mpl_toolkits.axisartist as axisartist
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# ax1 = plt.subplot(111, projection='polar')
# t=np.linspace(0,360,num=37,endpoint=True)
# x=[]
# for i in range(37):
#     x.append(math.radians(t[i]))
# y=[93.9,84.2,78.7,75.5,64.2,52.7,43.2,39.3,32.4,34.5,38.9,47.4,56.1,67.1,72.7,77.3,82.3,91.2,77.8,73.7,67.0,55.1,52.7,45.6,33.0,31.4,30.7,32.0,36.7,44.1,52.5,62.1,74.4,84.0,89.3,92.6,93.9]
# for i in range(37):
#     y[i]*=3.4
#     y[i]=round(y[i],1)
# print(y)
# ax=plt.subplot(111,projection='polar')
# ax.plot(x,y,r'o')
# ax.plot(x,y,r'-')
# ax.grid(True)
#
# plt.title('椭圆偏振光光强测量数据')
# plt.show()
#
#x=np.arange(0,360,10)
#y=[133.7,130.4,129.4,136.5,150.1,172.1,199.2,242,271,301,323,337,339,327,308,277,246,210,183,160,137.5,133.5,134.1,133.2,130.0,129.7,137.2,151.7,173.1,200.5,244,273,303,327,338,339]
cos=[0,0.03,0.12,0.25,0.41,0.59,0.75,0.88,0.97,1.00]
I_right=[-0.8, 5.0, 25.6, 60.6, 108.4, 168.2, 220.2, 260.2, 303.0, 306.7]
I=[0.8,3.3,12.3,27.5,48.3,74.3,96.9,114.3,132.9,134.5]
for i in I_right:
    i+=1.6
I_left=[0.87, 6.6, 27.6, 62.4, 110.3, 167.1, 222.1, 262.3,296.1, 308.9]
# plt.grid(True)
#
# plt.xlabel('$10^2$',fontproperties='SimHei',fontsize=14,verticalalignment='top')
# plt.title('光强与两透光夹角关系图')
# plt.show()
fig=plt.figure()
ax=axisartist.Subplot(fig,111)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"]=ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)
ax.axis["y"]=ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")
plt.plot(cos,I_right,label="右旋")
plt.plot(cos,I_left,label="左旋")
plt.text(1.05,0,r'$cos^2＠$',fontsize=14)
plt.text(-0.1,330,r'$I/1*10^7A$',fontsize=14)
plt.title("透过两偏振器后光强I与透光夹角关系")
plt.legend(loc='upper left')
x=[0,1]
y=[0,300]
plt.plot(x,y,color='black')
plt.grid(True)
plt.show()