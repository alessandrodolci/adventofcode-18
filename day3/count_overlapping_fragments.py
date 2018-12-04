fabric = [[]]
claims_count = 0
fragments_count = None
not_overlapping_id = None

with open("input.txt") as input_file:
    for line in input_file:
        tokens = line.split()
        claim_id = tokens[0]
        distance_string = tokens[2]
        size_string = tokens[3]

        start_column = int(distance_string[:distance_string.index(',')])
        start_row = int(distance_string[distance_string.index(',')+1:distance_string.index(':')])
        
        width = int(size_string[:size_string.index('x')])
        height = int(size_string[size_string.index('x')+1:])

        # Extending the fabric size, not necessary assuming a size of 1000 square inches
        for i in range(len(fabric), start_row+height):
            fabric.append([] * len(fabric[0]))
        for row in fabric:
            if len(row) < start_column+width:
                row.extend([[]] * (start_column+width-len(row)))
        
        # Adding up the current fragment
        for i in range(height):
            for j in range(width):
                if not fabric[start_row+i][start_column+j]:
                    fabric[start_row+i][start_column+j] = [claim_id]
                else:
                    fabric[start_row+i][start_column+j].append(claim_id)
 
        claims_count += 1

with open("input.txt") as input_file:
    for line in input_file:
        tokens = line.split()
        claim_id = tokens[0]
        not_overlapping = True
        for row in fabric:
            for column in row:
                if claim_id in column and len(column) > 1:
                    not_overlapping = False
        if not_overlapping == True:
            not_overlapping_id = claim_id
            break

fragments_count = 0
for row in fabric:
    for fragment in row:
        if len(fragment) >= 2:
            fragments_count += 1

print("Fragments with two or more claims: " + str(fragments_count)
    + "\nID of the non-overlapping claim: " + str(not_overlapping_id))
