import sys

def calculate_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

coordinates = []
total_area_edge_length = -1

with open("input.txt", "r") as input_file:
    for line in input_file:
        tokens = line.split()
        x = int(tokens[0][:tokens[0].index(',')])
        y = int(tokens[1])
        # Store the coordinates in inverse order to correctly access the matrix later ((row, column))
        coordinates.append((y, x))
        highest_coordinate = max(x, y)
        if highest_coordinate > total_area_edge_length:
            total_area_edge_length = highest_coordinate

min_i = min(coordinates, key = lambda t: t[0])[0]
min_j = min(coordinates, key = lambda t: t[1])[1]
max_i = max(coordinates, key = lambda t: t[0])[0]
max_j = max(coordinates, key = lambda t: t[1])[1]
infinite_coordinates = []
for index, coordinate in enumerate(coordinates):
    if coordinate[0] in [min_i, max_i] or coordinate[1] in [min_j, max_j]:
        infinite_coordinates.append(index)

distances = [['.' for i in range(total_area_edge_length)] for i in range(total_area_edge_length)]
for i in range(total_area_edge_length):
    for j in range(total_area_edge_length):
        best_distance = sys.maxsize
        for index, coordinate in enumerate(coordinates):
            distance = calculate_distance((i, j), coordinate)
            if distance < best_distance:
                best_distance = distance
                distances[i][j] = index
            elif distance == best_distance:
                distances[i][j] = '.'
        if distances[i][j] in infinite_coordinates:
            distances[i][j] = '.'

best_area_size = -1
coordinates_areas = {}
for distance in distances:
    for coordinate in distance:
        if coordinate != '.':
            coordinates_areas[str(coordinate)] = coordinates_areas.get(str(coordinate), 0) + 1

print(coordinates_areas)

print("Size of the largest area: " + str(max(coordinates_areas.values())))
