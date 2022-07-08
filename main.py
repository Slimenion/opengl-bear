# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Объявляем все глобальные переменные
global xrot         # Величина вращения по оси x
global zrot         # Величина вращения по оси y
global ambient      # рассеянное освещение
global greencolor   # Цвет елочных иголок
global treecolor    # Цвет елочного стебля
global mainColor
global lightpos     # Положение источника освещения


# Процедура инициализации
def init():
    global xrot         # Величина вращения по оси x
    global zrot         # Величина вращения по оси y
    global ambient      # Рассеянное освещение
    global greencolor   # Цвет елочных иголок
    global treecolor    # Цвет елочного ствола
    global mainColor
    global lightpos     # Положение источника освещения

    xrot = 0.0                          # Величина вращения по оси x = 0
    zrot = 0.0                          # Величина вращения по оси y = 0
    ambient = (1.0, 1.0, 1.0, 1)        # Первые три числа цвет в формате RGB, а последнее - яркость
    greencolor = (0.2, 0.8, 0.0, 0.8)  
    treecolor = (0.9, 0.6, 0.3, 0.8)  
    mainColor = (0.505882, 0.0941176, 0.00784314, 0.51)
    lightpos = (1.0, 1.0, 1.0)          # Положение источника освещения по осям xyz

    glClearColor(0.5, 0.5, 0.5, 1.0)              
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)                # Определяем границы рисования по горизонтали и вертикали
    glRotatef(-90, 1.0, 0.0, 0.0)
                       # Сместимся по оси Х на 90 градусов
    #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) # Определяем текущую модель освещения
    #glEnable(GL_LIGHTING)                           # Включаем освещение
    #glEnable(GL_LIGHT0)                             # Включаем один источник света
    #glLightfv(GL_LIGHT0, GL_POSITION, lightpos)


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global zrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:      # Клавиша вверх
        xrot -= 2.0             # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:    # Клавиша вниз
        xrot += 2.0             # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        zrot -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        zrot += 2.0             # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()         # Вызываем процедуру перерисовки


# Процедура перерисовки
def draw():
    global xrot
    global zrot
    global lightpos
    global greencolor
    global treecolor
    global mainColor

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                # Очищаем экран и заливаем серым цветом
    glPushMatrix()
    glEnable(GL_DEPTH_TEST)                                               # Сохраняем текущее положение "камеры"
    glRotatef(xrot, 1.0, 0.0, 0.0)                              # Вращаем по оси X на величину xrot
    glRotatef(zrot, 0.0, 0.0, 1.0)                              # Вращаем по оси Z на величину zrot
    #Основное тело
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glColor3f(0.6549019607, 0.3686274509, 0.1019607843)
    glutSolidSphere(0.4,20,20)
    #Голова
    glTranslatef(0.0,0.0,0.3)
    glutSolidSphere(0.3,20,20)
    #Нога правая
    glColor3f(0.1529411764,0.0980392156,0.0549019607)
    glTranslatef(0.0,0.1,-0.7)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,0.0,-0.1)
    glutSolidCylinder(0.1, 0.2, 20, 20)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,-0.1,0.8)
    #Нога левая
    glTranslatef(0.0,-0.1,-0.7)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,0.0,-0.1)
    glutSolidCylinder(0.1, 0.2, 20, 20)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,0.1,0.8)
    #рука правая
    glTranslatef(0.0,0.35,-0.2)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,0.0,-0.3)
    glutSolidCylinder(0.1, 0.3, 20, 20)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,-0.35,0.5)
    #рука левая
    glTranslatef(0.0,-0.35,-0.2)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,0.0,-0.3)
    glutSolidCylinder(0.1, 0.3, 20, 20)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,0.35,0.5)
    #ушко правое
    glTranslatef(0.0,0.2,0.25)
    glRotatef(90,0.0,1,0.0)
    glutSolidTorus(0.05,0.1,20,20)
    glColor3f(0.6549019607, 0.3686274509, 0.1019607843)
    glutSolidSphere(0.05,20,20)
    glRotatef(-90,0.0,1,0.0)
    glTranslatef(0.0,-0.2,-0.25)
    #ушко левое
    glColor3f(0.1529411764,0.0980392156,0.0549019607)
    glTranslatef(0.0,-0.2,0.25)
    glRotatef(90,0.0,1,0.0)
    glutSolidTorus(0.05,0.1,20,20)
    glColor3f(0.6549019607, 0.3686274509, 0.1019607843)
    glutSolidSphere(0.05,20,20)
    glRotatef(-90,0.0,1,0.0)
    glTranslatef(0.0,0.2,-0.25)
    #морда 
    glColor3f(0.1529411764,0.0980392156,0.0549019607)
    glTranslatef(0.2,0.0,0.04)
    glutSolidTorus(0.07,0.1,20,20)
    glTranslatef(0.0,0.0,0.025)
    glutSolidSphere(0.1,20,20)
    glTranslatef(0.0,0.0,-0.025)
    glTranslatef(-0.2,0.0,-0.04)
    #глаза
    #правый
    glColor3f(1,1,1)
    glTranslatef(0.2,0.15,0.15)
    glutSolidSphere(0.05,20,20)
    glTranslatef(0.04,0,0)
    glColor3f(0,0,0)
    glutSolidSphere(0.025,20,20)
    glTranslatef(-0.24,-0.15,-0.15)
    #левый
    glColor3f(1,1,1)
    glTranslatef(0.2,-0.15,0.15)
    glutSolidSphere(0.05,20,20)
    glTranslatef(0.04,0,0)
    glColor3f(0,0,0)
    glutSolidSphere(0.025,20,20)
    glTranslatef(-0.24,0.15,-0.15)


    

    glPopMatrix()                                               # Возвращаем сохраненное положение "камеры"
    glutSwapBuffers()                                           # Выводим все нарисованное в памяти на экран


# Здесь начинается выполнение программы
# Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
# Указываем начальный размер окна (ширина, высота)
glutInitWindowSize(300, 300)
# Указываем начальное положение окна относительно левого верхнего угла экрана
glutInitWindowPosition(50, 50)
# Инициализация OpenGl
glutInit(sys.argv)
# Создаем окно с заголовком
glutCreateWindow(b"Bear!")
# Определяем процедуру, отвечающую за перерисовку
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку клавиш
glutSpecialFunc(specialkeys)
# Вызываем нашу функцию инициализации
init()
# Запускаем основной цикл
glutMainLoop()