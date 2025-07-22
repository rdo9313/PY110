MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def after_midnight(time):
    hours, minutes = time.split(":")
    hours = int(hours) % HOURS_PER_DAY

    return hours * MINUTES_PER_HOUR + int(minutes)

def before_midnight(time):
    minutes = MINUTES_PER_DAY - after_midnight(time)
    return minutes % MINUTES_PER_DAY

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True