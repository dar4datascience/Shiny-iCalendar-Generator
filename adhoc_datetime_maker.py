import datetime
# use type hints
def make_datetime(date: datetime.date, str_time: str) -> datetime.datetime:
    """Function to jointly  create datetime object from date input and select input shiny. dateobject + string"""
    # time comes in the form of 1 PM, 2 PM, 3 PM, etc.
    time = datetime.datetime.strptime(str_time, '%I %p')
    # combine date and time
    datetime_object = datetime.datetime.combine(date, time.time())

    return datetime_object

if __name__ == '__main__':
    print(make_datetime(datetime.date(2021, 1, 1), '1 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '1 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '2 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '3 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '4 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '5 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '6 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '7 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '8 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '9 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '10 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '11 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '12 PM'))
    print(make_datetime(datetime.date(2021, 1, 1), '12 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '1 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '2 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '3 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '4 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '5 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '6 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '7 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '8 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '9 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '10 AM'))
    print(make_datetime(datetime.date(2021, 1, 1), '11 AM'))
