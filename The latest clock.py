# Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

# The time should be in HH:MM format.

# Examples:

# digits: 1, 9, 8, 3 => result: "19:38"
# digits: 9, 1, 2, 5 => result: "21:59"
# Notes
# Result should be a valid 24-hour time, between 00:00 and 23:59.
# Every input has a valid answer.

from itertools import permutations

def latest_clock(a, b, c, d):
    digits = [a, b, c, d]
    all_times = permutations(digits)

    latest_valid_time = "00:00"

    for time in all_times:
        hh = time[0] * 10 + time[1]
        mm = time[2] * 10 + time[3]

        if 0 <= hh < 24 and 0 <= mm < 60:
            current_time = f"{hh:02d}:{mm:02d}"

            if current_time > latest_valid_time:
                latest_valid_time = current_time

    return latest_valid_time

# Examples:
print(latest_clock(1, 9, 8, 3))  # Output: "19:38"
print(latest_clock(9, 1, 2, 5))  # Output: "21:59"