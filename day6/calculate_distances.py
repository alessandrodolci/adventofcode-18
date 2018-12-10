import sys

def calculate_distance(a, b):
    return abs((b[0] - a[0]) + (b[1] - a[1]))

coordinates = []
total_area_edge_length = -1

with open("input.txt", "r") as input_file:
    for line in input_file:
        tokens = line.split()
        x = int(tokens[0][:tokens[0].index(',')])
        y = int(tokens[1])
        coordinates.append((x, y))
        highest_coordinate = max(x, y)
        if highest_coordinate > total_area_edge_length:
            total_area_edge_length = highest_coordinate

distances = [['' for i in range(total_area_edge_length)] for i in range(total_area_edge_length)]
for i in range(total_area_edge_length):
    for j in range(total_area_edge_length):
        best_distance = sys.maxsize
        for index, coordinate in enumerate(coordinates):
            distance = calculate_distance((i, j), coordinate)
            if distance < best_distance:
                best_distance = distance
                distances[i][j] = index

best_area_size = -1
coordinates_areas = {}
for distance in distances:
    for coordinate in distance:
        coordinates_areas[str(coordinate)] = coordinates_areas.get(str(coordinate), 0) + 1

print("Size of the largest area: " + str(max(coordinates_areas.values())))
