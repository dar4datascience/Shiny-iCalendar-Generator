import qrcode
img = qrcode.make('''
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//My calendar product//example.com//
BEGIN:VEVENT
SUMMARY:Awesome Meeting
DTSTART:20230125T080000Z
DTEND:20230125T090000Z
DESCRIPTION:Define the roadmap of our awesome project
LOCATION:Mexico City\, Mexico
TITLE:My cool event
END:VEVENT
END:VCALENDAR
''')
type(img)
img.save("vcal.png")


# BEGIN:VCALENDAR
# VERSION:2.0
# BEGIN:VEVENT
# SUMMARY:Lunchtime meeting
# DTSTART;TZID=America/New_York:20230420T120000
# DURATION:PT1H
# LOCATION:Meeting Room 1
# END:VEVENT
# END:VCALENDAR