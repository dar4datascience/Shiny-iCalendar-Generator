# imports
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
# import time delta
from datetime import timedelta
from pathlib import Path
import os
import pytz
 
# init the calendar
cal = Calendar()

# Some properties are required to be compliant
cal.add('prodid', '-//My calendar product//example.com//')
cal.add('version', '2.0')

start_time = datetime(2023, 1, 25, 8, 0, 0, tzinfo=pytz.utc)
end_time = start_time + timedelta(hours=1)

# Add subcomponents
event = Event()
event.add('title', 'My cool event') # doesnt appear
event.add('summary', 'Awesome Meeting') # appears as title in google
# time delta of 1 hour
#event.add('duration', timedelta(hours=1))
# appears
event.add('description', 'Define the roadmap of our awesome project')
event.add('dtstart', start_time)
event.add('dtend', end_time)

# # Add the organizer
# organizer = vCalAddress('MAILTO:jdoe@example.com')
 
# # Add parameters of the event
# organizer.params['name'] = vText('John Doe')
# organizer.params['role'] = vText('CEO')
# event['organizer'] = organizer
# appreas
event['location'] = vText('Mexico City, Mexico')

# Add the event to the calendar
cal.add_component(event)

f = open('example.ics', 'wb')
f.write(cal.to_ical())
f.close()