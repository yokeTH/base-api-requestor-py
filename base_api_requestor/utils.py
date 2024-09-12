import datetime
import time
import string
import random


def wait_for_time(date_time):
    t = time_string_to_datetime(date_time)
    while True:
        print('Now:', datetime.datetime.now())
        if datetime.datetime.now() > t:
            break
        time.sleep(1)


def time_string_to_datetime(time_string):
    return datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')


def join_url_parts(*args):
    return "/".join(str(arg).strip("/") for arg in args)


def generate_random_string(length=4):
    characters = string.ascii_lowercase + string.digits
    return "".join(random.choice(characters) for _ in range(length))
