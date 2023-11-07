from icalendar import Calendar, Event, vText
from datetime import datetime, timedelta
import pytz
import qrcode
import tempfile

def create_event_qr(start_time, title):
    # init the calendar
    cal = Calendar()

    # Some properties are required to be compliant
    cal.add('prodid', '-//My calendar product//example.com//')
    cal.add('version', '2.0')

    end_time = start_time + timedelta(hours=1)

    # Add subcomponents
    event = Event()
    event.add('summary', title) # appears as title in google
    event.add('description', 'Define the roadmap of our awesome project')
    event.add('dtstart', start_time)
    event.add('dtend', end_time)
    event['location'] = vText('Mexico City, Mexico')

    # Add the event to the calendar
    cal.add_component(event)

    #You can generate a string for a file with the to_ical() method:
    calendar_string = cal.to_ical()

    img = qrcode.make(calendar_string)

    # Generate filename from event title and start time
    filename = f"{title.replace(' ', '_')}_{start_time.strftime('%Y%m%d%H%M')}.png"

    # Create a temporary file
    _, temp_file_name = tempfile.mkstemp()

    # Append .png extension to temp file
    temp_file_name = f"{temp_file_name}_{filename}"

    # Save the image to the temporary file
    img.save(temp_file_name)

    print(f'Temporary file has been created at {temp_file_name}')

    return temp_file_name

# Test the function using if __name__ == '__main__'
if __name__ == '__main__':

    start_time = datetime(2023, 1, 25, 8, 0, 0, tzinfo=pytz.utc)
    temp_file_name = create_event_qr(start_time, 'My cool event')