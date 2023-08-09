class_points_test = [41, 75, 72, 56, 80, 82, 81, 33]
your_points_test = 50


def better_than_average(class_points, your_points):
    total = 0
    for point in class_points:
        print(point)
        total += point
    class_average = total / len(class_points)
    print(class_average)
    print(len(class_points))
    if your_points >= class_average:
        return True
    else:
        return False


print(better_than_average(class_points_test, your_points_test))