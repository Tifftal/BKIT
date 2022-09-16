import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    while(True):
        try:
        # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
        # Вводим с клавиатуры
            print(prompt)
        coef_str = input()
        # Переводим строку в действительное число
        try:
            coef = float(coef_str)
            if index != 1: return coef
            if coef != 0 and index == 1:
                return coef
            else:
                print('Некорректное значение коэффициента, попробуйте снова')
        except:
            print('Некорректное значение коэффициента, попробуйте снова\nДля введения числа с дробной частью используйте "."  (0,5=0.5)')



def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    #print('D=', D)
    '''
    Уравнение: ax^4+bx^2+c=0
    Замена: t=x^2    =>   
    at^2+bt+c=0
    D=b^2+4ac
    D=0                                                         D>0
    t=-b/2a                                 t1=(-b-sqrt(D))/2a                  t2=(-b+srqt(D))/2a
    если t>=0                               если t1>=0                          если t2>=0
    x1=-sqrt(t)     x2=+sqrt(t)             x3=-sqrt(t1)    x4=+sqrt(t1)        x5=-sqrt(t2)    x6=+sqrt(t2)
    
    
    Добавить проверку на совпадение корней!
    '''
    if D == 0.0:
        t = -b / (2.0 * a)
        if t >= 0:
            sq_t = math.sqrt(t)
            #print('sq_t=',sq_t)
            root1 = (-1.0) * sq_t
            root2 = sq_t
            #print('x1=', root1, 'x2=', root2)
            if root1!=root2:
                result.append(root1)
                result.append(root2)
            else:
                result.append(root1)
    elif D > 0.0:
        sqD = math.sqrt(D)
        #print(sqD)
        t1 = (-b + sqD) / (2.0 * a)
        t2 = (-b - sqD) / (2.0 * a)
        #print('t1=', t1,'  t2=', t2)

        if t1>=0:
            sq_t1 = math.sqrt(t1)
            #print('sq_t1=', sq_t1)
            root3 = (-1.0) * sq_t1
            root4 = sq_t1
            #print('x3=', root3, 'x4=', root4)
            if root3!=root4:
                result.append(root3)
                result.append(root4)
            else:
                result.append(root3)
            #result.append(root3)
            #result.append(root4)

        if t2>=0:
            sq_t2 = math.sqrt(t2)
            #print('sq_t2=', sq_t2)
            root5 = (-1.0) * sq_t2
            root6 = sq_t2
            #print('x5=', root5, 'x6=', root6)
            if root5!=root6:
                result.append(root5)
                result.append(root6)
            else:
                result.append(root5)
            #result.append(root5)
            #result.append(root6)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    #print('Уравнение:', a, 'x^4 + ', b, 'x^2 + ', c, ' = 0', sep='')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {}; {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}; {}; {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}; {}; {}; {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
