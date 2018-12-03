import sys

with open("input.txt", "r") as first_input_file:
    for first_line in first_input_file:
        with open("input.txt", "r") as second_input_file:
            for second_line in second_input_file:
                for i in range(len(first_line)-1):
                    if first_line[i] != second_line[i]:
                        first_substring = first_line[0:i] + first_line[i+1:]
                        second_substring = second_line[0:i] + second_line[i+1:]
                        print("\n\n" + first_substring)
                        print(second_substring)
                        if first_substring == second_substring:
                            print("Letters in common: " + first_substring)
                            sys.exit(0)

print("No matching substring found")
sys.exit(0)