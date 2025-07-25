import random

valid_chars = '0123456789abcdef'

def random_uuid(length):
    return "".join(random.choice(valid_chars) for _ in range(length))

def create_uuid():
    return "-".join([random_uuid(8), random_uuid(4), random_uuid(4), random_uuid(4), random_uuid(12)])

create_uuid()