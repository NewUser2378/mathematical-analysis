import numpy as np

def integral_function(x, y):
    return x * y**2 - x**2 * y


def sum_integral_function(x_step,y_step):# Определяем функцию с шагами итерации по x и по y
    total_sum = 0
    x=0
    y=0
    # Итерируем по точкам (x, y) в пределах x² + y² <= 9, x > 0
    while(x**2 + y**2 <= 9 ): # Проверяем условие x² + y² <= 9 то есть что наши значения внутри ломанной, то есть со звеньями все хорошо
        y=0 #бнуляем значение y и считаем все значения для данного x
        while (x ** 2 + y ** 2 <= 9): # Проверяем условие после сбавления шага
                # Вычисляем значение функции и добавляем его к общей сумме
            total_sum +=  integral_function(x , y)

            y+=y_step
        x += x_step

    return total_sum

def center_point_value(x, y, d):#считаем координаты центра
    center_x = x + d / 2
    center_y = y + d / 2
    return integral_function(center_x, center_y)

def sum_cube_function(  d):#находим функцию для разбиения на кубы
    total_sum = 0
    x = 0
    y = 0

    while (x**2 + y**2 <= 9): #проверяем условие того что находимся внутри фигуры

        total_sum += center_point_value(x, y, d)
        y += d #переходим к следующим кубам
        x += d

    return total_sum



# Пример использования для разбиения d = 0.01
result = sum_integral_function(0.01,0.01)
print(result)
