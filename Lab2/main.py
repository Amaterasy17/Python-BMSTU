from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
import bcrypt 


def main():
    print("ИУ5-51Б Шевчук Михаил Лаб_2")

    rectangle = Rectangle("желтого", 1, 2)
    circle = Circle("розового", 3)
    square = Square("черного", 4)

    print(rectangle)
    print(circle)
    print(square)
    print(bcrypt.hashpw('ИУ5-51Б Шевчук Михаил Лаб_2'.encode(), bcrypt.gensalt()))

if __name__ == "__main__":
    main()
