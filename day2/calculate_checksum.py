with open("input.txt", "r") as input_file:
    two_occurences = 0
    three_occurences = 0
    for line in input_file:
        already_counted = []
        two_occurences_found = False
        three_occurences_found = False
        for char in line:
            if char not in already_counted:
                if line.count(char) == 2 and two_occurences_found == False:
                    two_occurences += 1
                    two_occurences_found = True
                elif line.count(char) == 3 and three_occurences_found == False:
                    three_occurences += 1
                    three_occurences_found = True
                already_counted.append(char)
                print(already_counted)

checksum = two_occurences * three_occurences

print("Number of two characters occurences: " + str(two_occurences)
    + "\nNumber of three characters occurences: " + str(three_occurences)
    + "\nChecksum: " + str(checksum))