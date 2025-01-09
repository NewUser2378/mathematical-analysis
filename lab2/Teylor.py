import math
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
ax.set_title('Многочлены Тейлора')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
x=np.linspace(-10,10,1000)#разбиваем на 1000  узлов и берем промежуток от 0 до точкии a из условия
y0=np.cos(x+math.pi/6)
y=((math.sqrt(3))/2)+(-0.5)*x
y1=((math.sqrt(3))/2)+(-0.5)*x-((math.sqrt(3))/4)*(x**2)
y2=((math.sqrt(3))/2)+(-0.5)*x-((math.sqrt(3))/4)*(x**2)+(x**3)/12
ax.plot(x,y0,color='red',label="исходная фуекция")#
ax.plot(x,y,label="при n=1")
ax.plot(x,y1,label="при n=2")
ax.plot(x,y2,alpha =0.5,color = 'green',label="при n=3")#уменьшим прозрачность так как график почти совпадает с предыдущим

plt.legend()
plt.show()
n1=((math.sqrt(3))/2)+(-0.5)*0.05-((math.sqrt(3))/4)*(0.05**2) #пункт 2,выводим приближенные значения
n2=((math.sqrt(3))/2)+(-0.5)*0.05-((math.sqrt(3))/4)*(0.05**2)+(0.05**3)/12
print(n1,n2)
print(n1-math.cos(0.05+math.pi/6))#пункт 3 , считаем разницу,откуда получим совпадение с теоретической частью

print(n2-math.cos(0.05+math.pi/6))