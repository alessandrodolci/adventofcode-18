fabric = [[0]]

with open("input.txt") as input_file:
    for line in input_file:
        tokens = line.split()
        distance_string = tokens[2]
        size_string = tokens[3]

        start_column = int(distance_string[:distance_string.index(',')])
        start_row = int(distance_string[distance_string.index(',')+1:distance_string.index(':')])
        
        width = int(size_string[:size_string.index('x')])
        height = int(size_string[size_string.index('x')+1:])

        # Extending the fabric size, not necessary assuming a size of 1000 square inches
        for i in range(len(fabric), start_row+height):
            fabric.append([0] * len(fabric[0]))
        for row in fabric:
            if len(row) < start_column+width:
                row.extend([0] * (start_column+width-len(row)))
        
        # Adding up the current fragment
        for i in range(height):
            for j in range(width):
                fabric[start_row+i][start_column+j] += 1

result = 0
for row in fabric:
    for fragment in row:
        if fragment >= 2:
            result += 1

print(result)