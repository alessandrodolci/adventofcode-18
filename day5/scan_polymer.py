last_read = ''
with open("input.txt", "r") as input_file:
    with open("temp.txt", "w") as output_file:
        for line in input_file:
            output_file.write(line)

modified = True
while modified == True:
    with open("temp.txt", "r") as input_file:
        with open("output.txt", "w") as output_file:
            modified = False
            last_read = ''
            for line in input_file:
                for char in line:
                    if char != last_read.swapcase():
                        output_file.write("%s" %last_read)
                        last_read = char
                    else:
                        print(last_read + ' ' + char)
                        last_read = ''
                        if modified == False:
                            modified = True
            output_file.write("%s" %last_read)
    with open("output.txt", "r") as temp_input_file:
        with open("temp.txt", "w") as temp_output_file:
            for line in temp_input_file:
                temp_output_file.write(line)

units = 0
with open("output.txt", "r") as input_file:
    for line in input_file:
        for char in line:
            units += 1

print("Number of remaining units: " + str(units))