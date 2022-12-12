import math


def find_quadrilateral_area(A, B, C, D):
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]
    x3, y3 = C[0], C[1]
    x4, y4 = D[0], D[1]

    area = (x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1) - (y1 * x2 + y2 * x3 + y3 * x4 + y4 * x1)
    area = abs(area * 0.5)
    return area


def slope(A, B):
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]

    try:
        s = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        s = 0.001

    return s


def shape_and_area(Aq, Bq, Cq, Dq):
    area = find_quadrilateral_area(Aq, Bq, Cq, Dq)

    AB = math.dist(Aq, Bq)
    BC = math.dist(Bq, Cq)
    CD = math.dist(Cq, Dq)
    AD = math.dist(Aq, Dq)
    AC = math.dist(Aq, Cq)
    BD = math.dist(Bq, Dq)

    slope_prod1 = (slope(Aq, Dq)) * (slope(Bq, Cq))
    slope_prod2 = (slope(Aq, Bq)) * (slope(Cq, Dq))

    if area == 0:
        print("not a quadrilateral, points are collinear")
    else:

        if AB == BC and BC == CD and CD == AD and AB == AD:
            if AC == BD:
                # equal diagonals
                print("Square  " + str(area))
            else:
                print("Rhombus  " + str(area))
        elif AB == CD and BC == AD and AB != BC and CD != AD:
            if AC == BD:
                # equal diagonals
                print("Rectangle  " + str(area))
            else:
                print("Parallelogram  " + str(area))
        elif (slope_prod1 == 0 and AD != BC) or (slope_prod2 == 0 and AB != CD):
            # check if opposite sides parallel and unequal
            print("Trapezoid  " + str(area))
        elif (AB == BC and AD == CD and AB != CD) or (AB == AD and BC == CD and AB != CD):
            print("Kite  " + str(area))
        else:
            print("Others  " + str(area))


a1 = int(input("Enter the X co-ordinate of the first point:"))
a2 = int(input("Enter the Y co-ordinate of the first point:"))
b1 = int(input("Enter the X co-ordinate of the second point:"))
b2 = int(input("Enter the Y co-ordinate of the second point:"))
c1 = int(input("Enter the X co-ordinate of the third point:"))
c2 = int(input("Enter the Y co-ordinate of the third point:"))
d1 = int(input("Enter the X co-ordinate of the fourth point:"))
d2 = int(input("Enter the Y co-ordinate of the fourth point:"))

Aq = [a1, a2]
Bq = [b1, b2]
Cq = [c1, c2]
Dq = [d1, d2]

print(f'The co-ordinates are: {Aq},{Bq},{Cq},{Dq}')

shape_and_area(Aq, Bq, Cq, Dq)

# Test Cases
# Aq, Bq, Cq, Dq = [2,0], [0,2], [-2,0], [0,-5] --> Kite
# Aq, Bq, Cq, Dq = [0,0], [2,6], [6,6], [8,0] --> Trapezium
# Aq, Bq, Cq, Dq = [3,0], [4,5], [-1,4], [-2,-1] --> Rhombus
# Aq, Bq, Cq, Dq = [0,0], [2,4], [8,4], [6,0] --> Parallelogram
# Aq, Bq, Cq, Dq = [0,0], [0,4], [4,4], [4,0] --> Square
# Aq, Bq, Cq, Dq = [0,0], [0,4], [8,4], [8,0] --> Rectangle
