import math
import matplotlib.pyplot as plt
import numpy as np
figure =plt.figure()
ax1=figure.add_subplot(2,2,1)
ax1.grid(linewidth='0.5') #делаем сетку
ax1.set_xticks(np.arange(1,100,5) ) #делаем размеры сетки
ax1.set_yticks(np.arange(0,1,0.07) )
ax1.set_title('пункт 1')         #делаем названия для графиков
 #делаем названия осей
ax1.set_ylabel('Xn')
ax2=figure.add_subplot(2,2,2)
ax3=figure.add_subplot(2,2,3)
ax4=figure.add_subplot(2,2,4)
x=[]
y=[]
for i in range (1,101):
    x.append(i)
for j in range (1,101):
    y.append ((2*j-1)/(2*j+1)*math.sin(math.pi*(2+(-1)**j)/6))
ax1.plot(x,y,marker = '.',linestyle='--',linewidth='000.1',label = 'x_n') #делаем пунктирный стиль  и тонкий стиль линии, и отмечаем значения в целых точках
# так как не целые нам не интересны,ведь мы рассматриваем последовательность
sup_x=[]#так как супркмум и верхний предел совпадают,то построим для них общий график
x1=[]
for i in range (1,101):
    x1.append(i)
for j in range (1,101):
    sup_x.append (1)# добавляем 1 так ака это значение sin(pi/2)
ax1.plot(x1,sup_x,marker = '.',linestyle='--',linewidth='000.1',label = 'sup_x')
x2=[]
inf_x=[]
for i in range (1,101):
    x2.append(i)
for j in range (1,101):
    inf_x.append (1/3*1/2)# добавляем 1 так ака это значение 1/3*sin(pi/6)
ax1.plot(x2,inf_x,marker = '.',linestyle='--',alpha= 0.4,linewidth='000.1',label = 'sup_x')#делаем еще прозрачность ,чтобы увидеть точку от исходного графика
x3=[]
lowlimitx0=[]
for i in range (1,101):
    x3.append(i)
for j in range (1,101):
    lowlimitx0.append (1/2)# добавляем 1/2 так ака это значение sin(pi/6)
ax1.plot(x3,lowlimitx0,marker = '.',linestyle='--',linewidth='000.1')
ax2.set_xticks(np.arange(1,100,5) ) #делаем размеры сетки
ax2.set_yticks(np.arange(0,1,0.07) )
ax2.set_title('пункт 2')         #делаем названия для графиков
#делаем названия осей
ax2.set_ylabel('Yn')
ax2.grid(linewidth='0.5') #делаем сетку

x5=[]
y5=[]
for i in range (1,101):
    x5.append(i)
for j in range (1,101):
    y5.append ((2*j-1)/(2*j+1)*math.sin(math.pi*(2+(-1)**j)/6))
ax2.plot(x5,y5,marker = '.',linestyle='--',linewidth='000.1',label = 'x_n')
x4=[]
y_n=[]
for i in range (1,101,2):
    x4.append(i)
for j in range (1,101,2):
    y_n.append ((2*j-1)/(2*j+1)*0.5)  #добавляем значение подпоследовательности с нечетными номерами
ax2.plot(x4,y_n,marker = '.',linestyle='--',linewidth='000.1',label = 'y_n',alpha =0.35,color = 'red')#строим исходный график но уменьшаем прозрачность ,чтобы видеть подпоследовательность


e=float(input())
for j in range (1,200000000,1000):
    if (math.sin(math.pi/6)-e<(2*j-1)/(2*j+1)*math.sin(math.pi*(2+(-1)**j)/6)<math.sin(math.pi/6)+e):#достаточно проверить только это условие так как уже знаем,что подпоследовательность возрастает        n0=i
        n0=j
        break
ax3.grid(linewidth='0.5') #делаем сетку
ax3.set_xticks(np.arange(0,n0+100,10) ) #делаем размеры сетки
ax3.set_yticks(np.arange(0,1,0.07))
ax3.set_title('пункт 3')   #делаем названия для графиков
ax3.set_xlabel('n') #делаем названия осей
ax3.set_ylabel('Yn')
limitx0=[]
x7=[]
for i in range (n0,n0+101):
    x7.append(i)
for j in range (n0,n0+101):
    limitx0.append (1/2)# добавляем 1/2 так ака это значение sin(pi/6)
ax3.plot(x7,limitx0,marker = '.',linestyle='--',linewidth='000.1')
x8=[]
y6=[]
for i in range (n0,n0+101,2):
    x8.append(i)
for j in range (n0,n0+101,2):
    y6.append ((2*j-1)/(2*j+1)*math.sin(math.pi*(2+(-1)**j)/6))
ax3.plot(x8,y6,marker = '.',linestyle='--',linewidth='000.1',label = 'x_n')
ax4.grid(linewidth='0.5') #делаем сетку
ax4.set_xticks(np.arange(1,100,5) ) #делаем размеры сетки
ax4.set_yticks(np.arange(0,1,0.07) )
ax4.set_title('пункт 4')         #делаем названия для графиков
 #делаем названия осей
ax1.set_ylabel('Xn')
e1=float (input())#вводим эпсилон для 4 пункта
for j in range (1,200000000,1001):#делаем большой перебор (тк не требуется первый такой номер) шаг нечетный тк должны быть все значения из обоих подпоследовательностей
    if (math.sin(math.pi/2)-e1<(2*j-1)/(2*j+1)*math.sin(math.pi*(2+(-1)**j)/6)):#взяли верхнюю грань
        m=j
        break
m_=[]
m_.append(m)
x_m=[]
x_m.append((2*m-1)/(2*m+1)*math.sin(math.pi*(2+(-1)**m)/6))
ax4.plot(m_,x_m,marker = '.',color='red')
#теперь построим график как в 2 пункте(100 точек),но начиная с номера m,также уменьшим прозрачность,чтобы было видно предыдущую точку
x5=[]
y5=[]
for i in range (m,m+101):
    x5.append(i)
for j in range (m,m+101):
    y5.append ((2*j-1)/(2*j+1)*math.sin(math.pi*(2+(-1)**j)/6))
ax4.plot(x5,y5,marker = '.',linestyle='--',linewidth='000.1',label = 'x_n',alpha =0.35)
x4=[]
y_n=[]
for i in range (m,m+101,2):
    x4.append(i)
for j in range (m,m+101,2):
    y_n.append ((2*j-1)/(2*j+1)*0.5)  #добавляем значение подпоследовательности с нечетными номерами
ax4.plot(x4,y_n,marker = '.',linestyle='--',linewidth='000.1',label = 'y_n',alpha =0.35,color = 'green')
plt.show()