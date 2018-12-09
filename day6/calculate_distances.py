
def calculate_distance(a, b):
    return (b[0] - a[0]) + (b[1] - a[1])

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

distances = []
for i in range(total_area_edge_length):
    for j in range(total_area_edge_length):
        for coordinate in coordinates:
            area_sizes.append(calculate_distance((i, j), coordinate))
            distances