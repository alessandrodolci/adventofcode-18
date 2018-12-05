import common

common.order_input("input.txt", "input_chronological.txt")

sleep_hours = common.get_sleep_hours("input_chronological.txt")

most_slept_minute = -1
asleep_guard = None
times_slept = 0
for guard in sleep_hours:
    for i in range (60):
        if sleep_hours[guard][i] > times_slept:
            most_slept_minute = i
            asleep_guard = guard[1:]
            times_slept = sleep_hours[guard][i]

print("Guard that is most frequently asleep on the same minute: " + asleep_guard
    + "\nMost slept minute: " + str(most_slept_minute))
print("Result: " + str(int(asleep_guard) * most_slept_minute))