result = None
first_repetition = None
frequency = 0
frequency_values = [frequency]

while first_repetition is None:
	with open("input.txt", "r") as input_file:
		for line in input_file:
			value = int(line[1:])
			
			if line[0] == '+':
				frequency += value
			else:
				frequency -= value
		
			print(str(frequency) + " " + str(first_repetition))	
			if frequency in frequency_values and first_repetition is None:
				first_repetition = frequency
			else:
				frequency_values.append(frequency)
		
		if result is None:
			result = frequency
		
print("Result: " + str(result) + "\nFirst repeated frequency value: " + str(first_repetition))

