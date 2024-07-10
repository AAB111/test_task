import sys
import math

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        center_x, center_y = map(float, file.readline().split())
        radius = float(file.readline().strip())
    return center_x, center_y, radius

def read_points_data(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

def point_position(circle_x, circle_y, radius, point_x, point_y):
    distance_squared = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
    radius_squared = radius ** 2
    if math.isclose(distance_squared, radius_squared):
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py <circle_file> <dot_file>")
        sys.exit(1)
    
    circle_file = sys.argv[1]
    dot_file = sys.argv[2]
    
    circle_x, circle_y, radius = read_circle_data(circle_file)
    points = read_points_data(dot_file)
    
    for x, y in points:
        print(point_position(circle_x, circle_y, radius, x, y))
