def jarvis1(points: list):
    min_x = float('inf')
    min_y = float('inf')
    start_index = None
    result = []

    for i, (x, y) in enumerate(points):
        if x < min_x or (x == min_x and y < min_y):
            min_x = x
            min_y = y
            start_index = i

    most_left_point = start_index
    result.append(points[most_left_point])
    current_index = most_left_point

    while True:
        next_point = points[(current_index + 1) % len(points)]
        next_index = (current_index + 1) % len(points)

        for i, point in enumerate(points):
            cross_product = ((next_point[1] - points[current_index][1]) * (point[0] - next_point[0])) - \
                            ((point[1] - next_point[1]) * (next_point[0] - points[current_index][0]))
            if cross_product > 0:
                next_point = point
                next_index = i

        result.append(next_point)
        if next_index == most_left_point:
            break
        else:
            current_index = next_index

    return result

def jarvis2(points: list):
    min_x = float('inf')
    min_y = float('inf')
    start_index = None
    result = []

    for i, (x, y) in enumerate(points):
        if x < min_x or (x == min_x and y < min_y):
            min_x = x
            min_y = y
            start_index = i

    most_left_point = start_index
    result.append(points[most_left_point])
    current_index = most_left_point

    while True:
        next_point = points[(current_index + 1) % len(points)]
        next_index = (current_index + 1) % len(points)

        for i, point in enumerate(points):
            cross_product = ((next_point[1] - points[current_index][1]) * (point[0] - next_point[0])) - \
                            ((point[1] - next_point[1]) * (next_point[0] - points[current_index][0]))

            if cross_product > 0:
                next_point = point
                next_index = i

            if cross_product == 0:
                if (points[current_index][0] < next_point[0] < point[0] or points[current_index][0] > next_point[0] > point[0] or
                    points[current_index][1] < next_point[1] < point[1] or points[current_index][1] > next_point[1] > point[1]):
                    next_point = point
                    next_index = i

        result.append(next_point)
        if next_index == most_left_point:
            break
        else:
            current_index = next_index

    return result

def main():
    list1 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

    print(jarvis1(list1))
    print(jarvis2(list1))

if __name__ == "__main__":
    main()