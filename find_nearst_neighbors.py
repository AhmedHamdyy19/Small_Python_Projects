def distance(p1, p2):
    dist = np.sqrt(np.power(p1[0]-p2[0], 2) + np.power(p1[1]-p2[1], 2))
    return dist


def find_nearst_neighbors(points, p, k=5):
    dist = []
    for i in range(len(points)):
        dist.append(distance(points[i], p))

    sorted_points = points[np.argsort(dist)]
    return sorted_points[0:k]
