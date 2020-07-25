import requests
from datetime import datetime, timedelta

# API call to get the sunrise and sunset times with arguments -> South Africa's latitude and longitude , and date is today
url = "https://api.sunrise-sunset.org/json?lat=33.903800&lng=18.419742&date=today"

payload = {}
headers = {}

# Get response from request
response = requests.request("GET", url, headers=headers, data=payload)

# change response into json
a = response.json()

# strip sunrise from json object (UTC)
sunrise = a['results']['sunrise']
# strip sunset from json object (UTC)
sunset = a['results']['sunset']

# function used to format time into a hh:mm:ss format
def format_to_24hr(twelve_hour_time):
    return datetime.strftime(
        datetime.strptime(
            twelve_hour_time, '%I:%M:%S %p'
        ), "%H:%M:%S")

# function to change UTC+0 to UTC+2 - RSA Local time
def add_two_hours(time_string):
    the_time = datetime.strptime(time_string, "%H:%M:%S")
    new_time = the_time + timedelta(hours=2)
    return new_time.strftime("%H:%M:%S")

#change to LCD output strings
def toStringLCD(time_string):
    the_time = datetime.strptime(time_string, "%H:%M:%S")
    return the_time.strftime("%H:%M:%S")

# convert sunrise and sunset from 12 to 24 hours UTC+0 time
sunrise_utc = format_to_24hr(sunrise)
sunset_utc = format_to_24hr(sunset)

# convert sunrise and sunset to UTC+2
sunriseUtc2 = add_two_hours(sunrise_utc)
sunsetUtc2 = add_two_hours(sunset_utc)

#get lcd output strings
sunrise_utc_2_lcd = toStringLCD(sunriseUtc2)
sunset_utc_2_lcd = toStringLCD(sunsetUtc2)

# Output times in UTC+0
print("Sunrise time is " + sunrise_utc)
print("Sunset time is " + sunset_utc)

# Output times in UTC+2
print("Local (UTC+2) Sunrise time is " + sunriseUtc2)
print("Local (UTC+2) Sunset time is " + sunsetUtc2)

#output LCD
print("LCD Output Sunrise : " + toStringLCD(sunriseUtc2))
print("LCD Output Sunset : " + toStringLCD(sunsetUtc2))

