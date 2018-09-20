from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

if __name__ == "__main__":
    R = Rectangle('Прямоугольник', 2, 3, 'синий')
    C = Circle('Круг', 5, 'зеленый')
    S = Square('Квадрат', 5, 'красный')

    print('{} \n{} \n{}'.format(R, C, S))



