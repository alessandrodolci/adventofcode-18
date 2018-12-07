last_read = ''
with open("input.txt", "r") as input_file:
    with open("temp.txt", "w") as output_file:
        for line in input_file:
            for char in line:
                if char != last_read.swapcase():
                    output_file.write("%s" %last_read)
                    last_read = char
                else:
                    last_read = ''

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
                        if modified == False:
                            modified = True
                    else:
                        last_read = ''