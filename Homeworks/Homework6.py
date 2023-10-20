"""На плоскости задано множество точек. Найти окружность наименьшей площади, внутри
которой находятся все точки множества. Если таких окружностей несколько, найти любую. В
качестве ответа нарисовать найденную окружность."""
from dataclasses import dataclass


@dataclass
class Point:
    x: float = 0
    y: float = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

@dataclass
class Disc:
    center: Point = Point()
    r: float = 0

    def __str__(self):
        return f"Окружность с центром в {self.center} и радиусом {self.r}."

@dataclass
class Line:
    a: float
    b: float
    c: float

def minDisc(mas: list[Point]) -> Disc:

    # Если точка одна, то описывающая окружность
    # и есть эта точка.
    if len(mas) == 1:
        return Disc(mas[0], 0)

    # Создаем начальную минимальную окружность, построенную
    # на двух первых точках.
    disc = createStartDisc(mas[0], mas[1])

    # Проходимся по всем точкам и меняем или не меняем
    # окружность в зависимости от того, вошла эта точка
    # в текущую окружность или нет.
    for i in range(2, len(mas)):

        # Если точка находится вне окружности,
        # то находим новую окружность, в которой эта
        # точка будет лежать на границе.
        if not isInsideDisc(mas[i], disc):
            disc = MinDiscWithPoint(mas[:i], mas[i])

    return disc

def createStartDisc(p1: Point, p2: Point) -> Disc:
    center = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    r = (abs(p2.x - p1.x)**2 + abs(p2.y - p1.y)**2)**0.5/2
    return Disc(center, r)

def isInsideDisc(p: Point, disc: Disc) -> bool:
    dist = (abs(p.x - disc.center.x) ** 2 + abs(p.y - disc.center.y) ** 2) ** 0.5
    return dist <= disc.r

def MinDiscWithPoint(mas: list[Point], p: Point) -> Disc:
    disc = createStartDisc(mas[0], p)

    for i in range(1, len(mas)):

        # Если точка находится вне окружности,
        # то находим новую окружность, в которой эта точка,
        # а также точка p будут лежать на границе.
        if not isInsideDisc(mas[i], disc):
            disc = MinDiscWith2Points(mas[:i], mas[i], p)

    return disc

def MinDiscWith2Points(mas: list[Point], p1: Point, p2: Point) -> Disc:
    disc = createStartDisc(p1, p2)

    for i in range(len(mas)):

        # Если точка находится вне окружности,
        # то создаем новую окружность, которая
        # включает две обязательные точки p1 и p2,
        # а также текущую точку.
        if not isInsideDisc(mas[i], disc):
            disc = createDiscAround3Points(mas[i], p1, p2)

    return disc

def createDiscAround3Points(p1: Point, p2: Point, p3: Point) -> Disc:

    # Создаем серединные перпендикуляры,
    # которые задают центр описанной окружности
    medPerp1 = createMedPerp(p1, p2)
    medPerp2 = createMedPerp(p2, p3)
    A1, B1, C1 = medPerp1.a, medPerp1.b, medPerp1.c
    A2, B2, C2 = medPerp2.a, medPerp2.b, medPerp2.c

    # Находим центр
    if B1 * A2 - B2 * A1 and A1:
        y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
        x = (-C1 - B1 * y) / A1
    else:
        # Прямые не могут быть параллельными, поэтому нет
        # смысла проверять на равенство нулю.
        y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
        x = (-C2 - B2 * y) / A2

    r = (abs(x - p1.x) ** 2 + abs(y - p1.y) ** 2) ** 0.5

    return Disc(Point(x, y), r)

def createMedPerp(p1: Point, p2: Point) -> Line:

    # Координаты точки на перпендикуляре
    x0 = (p1.x + p2.x)/2
    y0 = (p1.y + p2.y)/2

    # Координаты направляющего вектора
    v_x = p1.y - p2.y
    v_y = p2.x - p1.x

    # Общее уравнение прямой
    a = v_y
    b = -v_x
    c = y0*v_x - x0*v_y

    return Line(a, b, c)

def main():

    # На вход подается список чисел через пробел,
    # которые будут координатами точек: x1, y1, x2, y2...
    try:
        mas = list(map(float, input().split(" ")))

        # Если подали нечетное количество чисел вначале,
        # то у последней точки нет координаты y,
        # поэтому отбрасываем последний x.
        if len(mas) % 2 != 0:
            mas = mas[:-1]

        # Делаем из списка координат - список точек,
        # а также удаляем дубликаты точек, если такие имеются.
        mas = list(set(map(lambda coords: Point(coords[0], coords[1]), zip(mas[::2], mas[1::2]))))
        disc = minDisc(mas)

        print(disc)

    except ValueError:
        print("Необходимо вводить числа вида 4, -5.0, 0.3 через пробел")

# def test_minDisc():
#     assert minDisc([Point(0, 0)]) == Disc(Point(0, 0), 0)
#     assert minDisc([Point(0, 0), Point(2, 0)]) == Disc(Point(1, 0), 1)
#     assert minDisc([Point(1, 1), Point(-1, 1), Point(1, -1), Point(-1, -1)]) == Disc(Point(0, 0), 2**0.5)
#     assert minDisc([Point(1, 1), Point(-1, 1), Point(1, -1), Point(-1, -1), Point(0, 0)]) == Disc(Point(0, 0), 2**0.5)
#     assert minDisc([Point(5.2, 6.2), Point(5, 6), Point(4.7, 5.7),
#                     Point(4, 6), Point(5, 7), Point(6, 6)]) == Disc(Point(5, 6), 1)

# [Point(x=89, y=198), Point(x=346, y=274), Point(x=410, y=180)]
# Окружность с центром в Point(x=217.5, y=236.0) и радиусом 134.00093283257397.

#main()