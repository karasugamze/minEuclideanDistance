from math import sqrt

points = [(3, 144), (8, 12),(3,4)]


def euclideanDistance(points):
    distances = []

    for i in points:
        öklid = sqrt(i[0] ** 2 + i[1] ** 2)
        distances.append(öklid)

    print(min(distances))


euclideanDistance(points)