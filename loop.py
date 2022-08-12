import random
import string
import os

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    os.system(f'mkdir ~/{result_str}')
get_random_string(255)
os.system('python3 loop.py')
