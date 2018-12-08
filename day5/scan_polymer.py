import shutil
import string

def reduce_polymers(input_file_name, output_file_name, char_to_exclude = ''):
    shutil.copyfile(input_file_name, "temp.txt")

    last_read = ''
    modified = True
    while modified == True:
        with open("temp.txt", "r") as input_file:
            with open(output_file_name, "w") as output_file:
                modified = False
                last_read = ''
                
                for line in input_file:
                    for char in line:
                        if char != last_read.swapcase() and char != char_to_exclude and char != char_to_exclude.swapcase():
                            output_file.write("%s" %last_read)
                            last_read = char
                        elif char != char_to_exclude and char != char_to_exclude.swapcase():
                            last_read = ''
                            if modified == False:
                                modified = True
                
                output_file.write("%s" %last_read)
        if modified == True:
            shutil.copyfile(output_file_name, "temp.txt")

def count_units(input_file_name):
    units = 0

    with open(input_file_name, "r") as input_file:
        for line in input_file:
            for char in line:
                units += 1

    return units

reduce_polymers("input.txt", "output.txt")

units = count_units("output.txt")

best_length = units
for char in string.ascii_lowercase:
    reduce_polymers("input.txt", "output.txt", char)
    current_units = count_units("output.txt")
    if (current_units < best_length):
        best_length = current_units

print("Number of remaining units: " + str(units))
print("Number of units in the best case: " + str(best_length))