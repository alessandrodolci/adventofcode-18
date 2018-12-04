import time

def order_input(file_name):
    input_file = open(file_name, "r")
    output_file = open("input_chronological.txt", "w")
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

order_input("input.txt")

with open("input_chronological.txt", "r") as input_file:
    sleep_hours = {}
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

most_asleep_guard = None
most_minutes_slept = 0
for guard in sleep_hours:
    guard_minutes_slept = 0
    times_slept = 0
    for i in range(60):
        guard_minutes_slept += sleep_hours[guard][i]
        if sleep_hours[guard][i] > times_slept:
            times_slept = sleep_hours[guard][i]
    if guard_minutes_

print(guard_most_slept_minute)slept > most_minutes_slept:
        most_asleep_guard = guard
        most_minutes_slept = guard_minutes_slept

most_asleep_guard = int(most_asleep_guard[1:])

guard_most_slept_minute = -1
guard_most_times_slept = 0
for i in range(60):
    if sleep_hours[guard][i] > guard_most_times_slept:
        guard_most_slept_minute = i
        guard_most_times_slept = sleep_hours[guard][i]

print("Result: " + str(most_asleep_guard * guard_most_slept_minute))