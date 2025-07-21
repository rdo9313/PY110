DEGREE = "\u00B0"
MINUTES = 60
SECONDS = 60

def extract_decimal(number):
    return number - int(number)

def dms(number):
    degrees = int(number)
    minutes = int(extract_decimal(number) * MINUTES)
    seconds = int(extract_decimal(extract_decimal(number) * MINUTES) * SECONDS)

    return f"{degrees}{DEGREE}{minutes:02}'{seconds:02}\""

    

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")