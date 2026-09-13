import os
import platform
import calendar
from datetime import datetime, date


def environment_report():
    # Get information about the current operating system and Python version
    operating_system = platform.system()
    python_version = platform.python_version()

    # Get the current working directory
    working_directory = os.getcwd()

    # Check whether the student data file exists
    data_file = "data/students.txt"
    file_exists = os.path.exists(data_file)

    # Get the file size if the file exists
    if file_exists:
        file_size = os.path.getsize(data_file)
    else:
        file_size = 0

    # Build the environment report
    report = (
        f"Operating System: {operating_system}\n"
        f"Python Version: {python_version}\n"
        f"Working Directory: {working_directory}\n"
        f"Student Data File Exists: {file_exists}\n"
        f"Student Data File Size: {file_size} bytes"
    )

    return report


def date_report():
    # Get today's date and the current date and time
    today = date.today()
    current_time = datetime.now()

    # Choose a future date for the countdown
    future_date = date(today.year, 12, 31)

    # Calculate how many days remain until the future date
    days_until = (future_date - today).days

    # Get calendar information for the current year and month
    leap_year = calendar.isleap(today.year)
    days_in_month = calendar.monthrange(today.year, today.month)[1]

    # Build the date report
    report = (
        f"Today's Date: {today.strftime('%Y-%m-%d')}\n"
        f"Current Timestamp: {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Days Until {future_date}: {days_until}\n"
        f"Leap Year: {leap_year}\n"
        f"Days in Current Month: {days_in_month}"
    )

    return report