# time_stuff.py - Useful functions to convert the time output by datetime
# module into an easier to read format

import re


def twelve_hr_time(mtime: str) -> str:
    """
    Take time formatted in 24-hour (military time)
    and output it in 12-hour clock format
    ex: 13:00:00 -> 1:00 PM
    Required module: re
    :param mtime:24-hour time passed as string. Pass as str(mtime) if needed.
    :return: 12-hour time passed as string
    """
    # Time Regex
    time_regex = re.compile(r'''(\d\d):(\d\d):(\d\d)''')
    mo = re.search(time_regex, mtime)
    if mo:
        hour = mo.group(1)
        minute = mo.group(2)
        seconds = mo.group(3)
        if int(hour) > 11:
            meridiem = 'PM'
        else:
            meridiem = 'AM'
        if int(hour) > 12:
            hour = int(hour) - 12
            hour = str(hour)
        elif hour == '00':
            hour = "12"
        new_time = f'{hour}:{minute}{meridiem}'
        return new_time



def format_time(dt: str, ea: str) -> str:
    """
    Take the time output by datetime.datetime.now or similar
    (expected year-month-day time(24 clock))
    and output an easy to read formatted time in the Euro style (d-m-y) or
    American style (m-d-y)
    The type is usually datetime.datetime, so pass the datetime arg as str(dt)
    Required modules: re
    :param dt:Datetime. please pass as str(dt) when calling this function
    :param ea: pass either 'EU' or 'US' (capitalization ignored)
    :return:Properly formatted string
    """
    # Time Regex to split out the data into variables
    time_regex = re.compile(r'''^((\d{4})-           # Year
                                (\d{2})-            # Month    
                                (\d{2})\s             # Day
                                (\d{2}:\d{2}:\d{2}) # Time
                                )''', re.VERBOSE)
    mo = re.search(time_regex, dt)
    if mo:
        year = mo.group(2).strip()
        month = mo.group(3).strip()
        day = mo.group(4).strip()
        time = twelve_hr_time(str(mo.group(5).strip()))
        if ea.casefold() == 'eu':
            new_date = f'{day}-{month}-{year} {time}'
        elif ea.casefold() == 'us':
            new_date = f'{month}-{day}-{year} {time}'
        else:
            print(f'{ea} is an invalid argument. No change was made.')
            new_date = dt
        return new_date
