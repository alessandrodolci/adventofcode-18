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

infinite_coordinates = []
distances = [['' for i in range(total_area_edge_length)] for i in range(total_area_edge_length)]
for i in range(total_area_edge_length):
    for j in range(total_area_edge_length):
        best_distance = sys.maxsize
        for index, coordinate in enumerate(coordinates):
            if index not in infinite_coordinates:
                distance = calculate_distance((i, j), coordinate)
                if distance < best_distance:
                    best_distance = distance
                    distances[i][j] = index
        if i == 0 or i == total_area_edge_length-1 or j == 0 or j == total_area_edge_length-1:
            infinite_coordinates.append(distances[i][j])

for i in range(total_area_edge_length):
    for j in range(total_area_edge_length):
        if distances[i][j] in infinite_coordinates:
            distances[i][j] = "inf"

print(distances)

best_area_size = -1
coordinates_areas = {}
for distance in distances:
    for coordinate in distance:
        if coordinate not in infinite_coordinates:
            coordinates_areas[str(coordinate)] = coordinates_areas.get(str(coordinate), 0) + 1

print(coordinates_areas)

print("Size of the largest area: " + str(max(coordinates_areas.values())))
