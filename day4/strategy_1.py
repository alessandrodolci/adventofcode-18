import common

common.order_input("input.txt", "input_chronological.txt")

sleep_hours = common.get_sleep_hours("input_chronological.txt")

most_asleep_guard = None
most_minutes_slept = 0
for guard in sleep_hours:
    guard_minutes_slept = 0
    for i in range(60):
        guard_minutes_slept += sleep_hours[guard][i]
    if guard_minutes_slept > most_minutes_slept:
        most_asleep_guard = guard
        most_minutes_slept = guard_minutes_slept

guard_most_slept_minute = -1
guard_most_times_slept = 0
for i in range(60):
    if sleep_hours[most_asleep_guard][i] > guard_most_times_slept:
        guard_most_slept_minute = i
        guard_most_times_slept = sleep_hours[most_asleep_guard][i]

most_asleep_guard = int(most_asleep_guard[1:])

print("Result: " + str(most_asleep_guard * guard_most_slept_minute))