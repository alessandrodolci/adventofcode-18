import time

def order_input(source_file_name, dest_file_name):
    input_file = open(source_file_name, "r")
    output_file = open(dest_file_name, "w")
    dates = []
    # Dictionary to store references between timestamps and lines (could be improved)
    date_lines = {}

    for line in input_file:
        tokens = line.split()
        date_string = (tokens[0] + ' ' + tokens[1])[1:len(tokens[0])+len(tokens[1])]
        dates.append(time.strptime(date_string, "%Y-%m-%d %H:%M"))
        date_lines[date_string] = line
    
    dates.sort()
    for date in dates:
        date = time.strftime("%Y-%m-%d %H:%M", date)
        output_file.write("%s" %date_lines[date])
    
    return

def get_sleep_hours(source_file_name):
    sleep_hours = {}

    with open(source_file_name, "r") as input_file:
        current_guard = None
        sleep_start = None
        sleep_end = None

        for line in input_file:
            tokens = line.split()

            if tokens[2] == "Guard":
                current_guard = tokens[3]
                if not current_guard in sleep_hours:
                    sleep_hours[current_guard] = {}
                    for i in range(60):
                        sleep_hours[current_guard][i] = 0
            elif tokens[2] == "falls":
                sleep_start = int(tokens[1][3:5])
            elif tokens[2] == "wakes":
                sleep_end = int(tokens[1][3:5])
                for i in range(sleep_start, sleep_end):
                    sleep_hours[current_guard][i] += 1
    
    return sleep_hours